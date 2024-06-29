from rest_framework import serializers
from users.models import CustomUser, Address, ContactInfo, NormalUser
from nutritionists.models import Nutritionist
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import Group


class CustomUserRegisterSerializer(RegisterSerializer):
    """
    This serializer overrides the default RegisterSerializer of dj_rest_auth to include the is_nutritionist field.
    """
    email = serializers.EmailField(required=True)
    is_nutritionist = serializers.BooleanField(required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['email'] = self.validated_data.get('email', '') # Email verification is currently disabled in the project settings.
        data['is_nutritionist'] = self.validated_data.get('is_nutritionist', False)
        return data
    
    def save(self, request):
        """
        This save method creates a new CustomUser instance and links it to a Nutritionist or a NormalUser instance based on the is_nutritionist field.
        The first_name is primarily set to the username of the CustomUser instance and can be changed later.
        """
        user = super().save(request)
        user.is_nutritionist = self.cleaned_data.get('is_nutritionist')
        user.save()

        if user.is_nutritionist:
            nutritionist = Nutritionist.objects.create(user=user, first_name=user.username, last_name="")
            group, created = Group.objects.get_or_create(name='Nutritionist')
            user.groups.add(group)
        else:
            normal_user = NormalUser.objects.create(user=user, first_name=user.username, last_name="")
            group, created = Group.objects.get_or_create(name='NormalUser')
            user.groups.add(group)
            
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Standard ModelSerializer for CustomUser model.
    Separated from CustomUserRegisterSerializer to allow for different permissions and fields.
    """
    role = serializers.SerializerMethodField('get_role')
    role_id = serializers.SerializerMethodField('get_role_id')
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'role_id']

    def get_role(self, obj):
        return obj.groups.all()[0].name

    def get_role_id(self, obj):
        if obj.is_staff:
            return 0
        elif obj.is_nutritionist:
            nutritionist = Nutritionist.objects.get(user=obj)
            return nutritionist.id
        else:
            normal_user = NormalUser.objects.get(user=obj)
            return normal_user.id



    
class AddressSerializer(serializers.ModelSerializer):
    """
    Standard ModelSerializer for Address model.
    """
    class Meta:
        model = Address
        fields = '__all__'

class ContactInfoSerializer(serializers.ModelSerializer):
    """
    Standard ModelSerializer for ContactInfo model.
    """
    class Meta:
        model = ContactInfo
        fields = '__all__'

class NormalUserSerializer(serializers.ModelSerializer):
    """
    ModelSerializer for NormalUser model.
    """
    user_id = serializers.IntegerField(write_only=True, required=False)
    user = serializers.StringRelatedField(read_only=True)
    address = AddressSerializer(many=True, required=False)
    contact_info = ContactInfoSerializer(many=True, required=False)

    class Meta:
        model = NormalUser
        fields = '__all__'
    
    def update(self, instance, validated_data):
        """
        This update method is overridden to exclude the possibility of changing the user_id and user fields.
        Since the related Address and ContactInfo instances are ManyToMany fields and cannot utilize CASCADE,
        they are deleted and recreated with the new data.
        """
        validated_data.pop('user_id', None)
        validated_data.pop('user', None)
        address_data = validated_data.pop('address', [])
        contact_info_data = validated_data.pop('contact_info', [])
        nutritionists_data = validated_data.pop('nutritionists', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if address_data is not None:
            instance.address.all().delete()
            for address in address_data:
                addr = Address.objects.create(**address)
                instance.address.add(addr)

        if contact_info_data is not None:
            instance.contact_info.all().delete()
            for contact_info in contact_info_data:
                contact = ContactInfo.objects.create(**contact_info)
                instance.contact_info.add(contact)

        if nutritionists_data is not None:
            instance.nutritionists.set(nutritionists_data)

        instance.save()
        return instance