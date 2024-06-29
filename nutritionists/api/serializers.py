from rest_framework import serializers
from nutritionists.models import Nutritionist, Education
from users.api.serializers import AddressSerializer, ContactInfoSerializer
from measurements.api.serializers import BodyMeasurementSerializer, SegmentalBodyMeasurementSerializer, BiochemicalMeasurementSerializer, DiseasesSerializer, DietSerializer
from users.models import Address, ContactInfo, NormalUser


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"

class ClientListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    address = AddressSerializer(many=True, required=False)
    contact_info = ContactInfoSerializer(many=True, required=False)
    body_measurements = BodyMeasurementSerializer(many=True, read_only=True)
    segmental_body_measurements = SegmentalBodyMeasurementSerializer(many=True, read_only=True)
    biochemical_measurements = BiochemicalMeasurementSerializer(many=True, read_only=True)
    diseases = DiseasesSerializer(many=True, read_only=True)
    diet = DietSerializer(many=True, read_only=True)

    class Meta:
        model = NormalUser
        exclude = ['nutritionists']

class NutritionistSerializer(serializers.ModelSerializer):
    """
    Serializer for the Nutritionist model.
    """
    user = serializers.StringRelatedField(read_only=True)
    personal_address = AddressSerializer(many=True)
    office_address = AddressSerializer(many=True)
    contact_info = ContactInfoSerializer(many=True)
    education = EducationSerializer(many=True)
    clients = ClientListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Nutritionist
        fields = "__all__"

    def create(self, validated_data):
        """
        This create method properly handles the creation of related Address, ContactInfo and Education instances.
        """
        personal_address_data = validated_data.pop('personal_address', [])
        office_address_data = validated_data.pop('office_address', [])
        contact_info_data = validated_data.pop('contact_info', [])
        education_data = validated_data.pop('education', [])

        nutritionist = Nutritionist.objects.create(**validated_data)

        for address_data in personal_address_data:
            address = Address.objects.create(**address_data)
            nutritionist.personal_address.add(address)

        for address_data in office_address_data:
            address = Address.objects.create(**address_data)
            nutritionist.office_address.add(address)

        for contact_info_item in contact_info_data:
            contact_info = ContactInfo.objects.create(**contact_info_item)
            nutritionist.contact_info.add(contact_info)

        for education_item in education_data:
            education = Education.objects.create(**education_item)
            nutritionist.education.add(education)

        return nutritionist
    
    def update(self, instance, validated_data):
        """
        This update method is overridden to exclude the possibility of changing the user_id and user fields.
        Since the related Address, ContactInfo and Education instances are ManyToMany fields and cannot utilize CASCADE,
        they are deleted and recreated with the new data.
        """
        validated_data.pop('user_id', None)
        validated_data.pop('user', None)
        personal_address_data = validated_data.pop('personal_address', None)
        office_address_data = validated_data.pop('office_address', None)
        contact_info_data = validated_data.pop('contact_info', None)
        education_data = validated_data.pop('education', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if personal_address_data is not None:
            instance.personal_address.all().delete()
            for address_data in personal_address_data:
                address = Address.objects.create(**address_data)
                instance.personal_address.add(address)

        if office_address_data is not None:
            instance.office_address.all().delete()
            for address_data in office_address_data:
                address = Address.objects.create(**address_data)
                instance.office_address.add(address)

        if contact_info_data is not None:
            instance.contact_info.all().delete()
            for contact_info_item in contact_info_data:
                contact_info = ContactInfo.objects.create(**contact_info_item)
                instance.contact_info.add(contact_info)

        if education_data is not None:
            instance.education.all().delete()
            for education_item in education_data:
                education = Education.objects.create(**education_item)
                instance.education.add(education)

        instance.save()
        return instance


class ClientCreateSerializer(serializers.ModelSerializer):
    """
    Serializer to handle the creation of a new client (NormalUser) instance.
    """
    address = AddressSerializer(many=True, required=False)
    contact_info = ContactInfoSerializer(many=True, required=False)

    class Meta:
        model = NormalUser
        # fields = '__all__'
        exclude = ['nutritionists']

    def create(self, validated_data):
        """
        This create method creates a client (NormalUser) instance and links it to the authenticated Nutritionist.
        This created NormalUser instance is not linked to a CustomUser instance.
        """
        address_data = validated_data.pop('address', [])
        contact_info_data = validated_data.pop('contact_info', [])

        normal_user = NormalUser.objects.create(**validated_data)

        for address in address_data:
            addr = Address.objects.create(**address)
            normal_user.address.add(addr)

        for contact_info in contact_info_data:
            contact = ContactInfo.objects.create(**contact_info)
            normal_user.contact_info.add(contact)

        request = self.context.get('request')
        nutritionist = request.user.nutritionist
        nutritionist.clients.add(normal_user)
        nutritionist.save()

        return normal_user
    
    def update(self, instance, validated_data):
        """
        This update method is overridden to exclude the possibility of changing the user_id and user fields.
        Since the related Address and ContactInfo instances are ManyToMany fields and cannot utilize CASCADE,
        they are deleted and recreated with the new data.
        """
        validated_data.pop('user_id', None)
        validated_data.pop('user', None)
        address_data = validated_data.pop('address', None)
        contact_info_data = validated_data.pop('contact_info', None)

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

        instance.save()
        return instance
    
    def delete(self, instance):
        """
        In this delete method, if the client (NormalUser) instance is linked to a CustomUser instance,
        the client is not deleted entirely from the database but only removed from the Nutritionist's clients list.
        If client is not linked to a CustomUser instance, the client is deleted entirely from the database.
        """
        if instance.user is not None:
            request = self.context.get('request')
            nutritionist = request.user.nutritionist
            nutritionist.clients.remove(instance)
        else:
            instance.delete()
        return instance
    
class UserToClientLinkSerializer(serializers.ModelSerializer):
    """
    This serializer is used to link an existing NormalUser to a Client.
    Only basic information data are linked to the Client.
    """
    # Todo - Implement the full link of the client to a NormalUser, including the CustomUser.
    user = serializers.StringRelatedField()
    address = AddressSerializer(many=True, required=False)
    contact_info = ContactInfoSerializer(many=True, required=False)

    class Meta:
        model = NormalUser
        fields = '__all__'

    def update(self, instance, validated_data):
        user = self.context.get('user') # Fetch the user object from the context
        if user is not None:
            try:
                normal_user = NormalUser.objects.get(user=user) # Fetch the NormalUser object related to the user
                client = instance
                # client.user = user # Link to CustomUser not implemented yet
                client.first_name = normal_user.first_name
                client.last_name = normal_user.last_name
                client.date_of_birth = normal_user.date_of_birth
                client.address.set(normal_user.address.all())
                client.contact_info.set(normal_user.contact_info.all())
                client.date_of_birth = normal_user.date_of_birth
                client.save()
            except NormalUser.DoesNotExist:
                raise serializers.ValidationError("The related user does not exist.")

        return instance