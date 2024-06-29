from rest_framework import serializers
from measurements.models import BodyMeasurement, SegmentalBodyMeasurement, BiochemicalMeasurement, Diseases, Diet
from users.models import NormalUser, CustomUser
from nutritionists.models import Nutritionist

"""
Standard ModelSerializers for their respective models.

The user field is not required and can be null to allow the association of the measurement 
with a nutritionist's client who isn't linked to a CustomUser instance.

The client field is not required and can be null to allow the association of the measurement 
to a CustomUser instance who isn't a nutritionist's client.
"""

class BodyMeasurementSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)
    client = serializers.PrimaryKeyRelatedField(queryset=NormalUser.objects.all(), required=False, allow_null=True)

    class Meta:
        model = BodyMeasurement
        fields = "__all__"

class SegmentalBodyMeasurementSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)
    client = serializers.PrimaryKeyRelatedField(queryset=NormalUser.objects.all(), required=False, allow_null=True)

    class Meta:
        model = SegmentalBodyMeasurement
        fields = "__all__"

class BiochemicalMeasurementSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)
    client = serializers.PrimaryKeyRelatedField(queryset=NormalUser.objects.all(), required=False, allow_null=True)

    class Meta:
        model = BiochemicalMeasurement
        fields = "__all__"

class DiseasesSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)
    client = serializers.PrimaryKeyRelatedField(queryset=NormalUser.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Diseases
        fields = "__all__"

class DietSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False, allow_null=True)
    client = serializers.PrimaryKeyRelatedField(queryset=NormalUser.objects.all(), required=False, allow_null=True)
    nutritionist = serializers.PrimaryKeyRelatedField(queryset=Nutritionist.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Diet
        fields = "__all__"

class AllClientMeasurementsSerializer(serializers.Serializer):
    body_measurements = serializers.SerializerMethodField()
    segmental_body_measurements = serializers.SerializerMethodField()
    biochemical_measurements = serializers.SerializerMethodField()
    diseases = serializers.SerializerMethodField()
    diet = serializers.SerializerMethodField()

    def get_body_measurements(self, obj):
        client_pk = self.context.get('client_pk')
        queryset = BodyMeasurement.objects.filter(client_id=client_pk)
        return BodyMeasurementSerializer(queryset, many=True).data

    def get_segmental_body_measurements(self, obj):
        client_pk = self.context.get('client_pk')
        queryset = SegmentalBodyMeasurement.objects.filter(client_id=client_pk)
        return SegmentalBodyMeasurementSerializer(queryset, many=True).data

    def get_biochemical_measurements(self, obj):
        client_pk = self.context.get('client_pk')
        queryset = BiochemicalMeasurement.objects.filter(client_id=client_pk)
        return BiochemicalMeasurementSerializer(queryset, many=True).data

    def get_diseases(self, obj):
        client_pk = self.context.get('client_pk')
        queryset = Diseases.objects.filter(client_id=client_pk)
        return DiseasesSerializer(queryset, many=True).data

    def get_diet(self, obj):
        client_pk = self.context.get('client_pk')
        queryset = Diet.objects.filter(client_id=client_pk)
        return DietSerializer(queryset, many=True).data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['body_measurements'] = self.get_body_measurements(instance)
        representation['segmental_body_measurements'] = self.get_segmental_body_measurements(instance)
        representation['biochemical_measurements'] = self.get_biochemical_measurements(instance)
        representation['diseases'] = self.get_diseases(instance)
        representation['diet'] = self.get_diet(instance)
        return representation

class AllUserMeasurementsSerializer(serializers.Serializer):
    body_measurements = serializers.SerializerMethodField()
    segmental_body_measurements = serializers.SerializerMethodField()
    biochemical_measurements = serializers.SerializerMethodField()
    diseases = serializers.SerializerMethodField()
    diet = serializers.SerializerMethodField()

    def get_body_measurements(self, obj):
        user_pk = self.context.get('user_pk')
        queryset = BodyMeasurement.objects.filter(user_id=user_pk)
        return BodyMeasurementSerializer(queryset, many=True).data

    def get_segmental_body_measurements(self, obj):
        user_pk = self.context.get('user_pk')
        queryset = SegmentalBodyMeasurement.objects.filter(user_id=user_pk)
        return SegmentalBodyMeasurementSerializer(queryset, many=True).data

    def get_biochemical_measurements(self, obj):
        user_pk = self.context.get('user_pk')
        queryset = BiochemicalMeasurement.objects.filter(user_id=user_pk)
        return BiochemicalMeasurementSerializer(queryset, many=True).data

    def get_diseases(self, obj):
        user_pk = self.context.get('user_pk')
        queryset = Diseases.objects.filter(user_id=user_pk)
        return DiseasesSerializer(queryset, many=True).data

    def get_diet(self, obj):
        user_pk = self.context.get('user_pk')
        queryset = Diet.objects.filter(user_id=user_pk)
        return DietSerializer(queryset, many=True).data
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['body_measurements'] = self.get_body_measurements(instance)
        representation['segmental_body_measurements'] = self.get_segmental_body_measurements(instance)
        representation['biochemical_measurements'] = self.get_biochemical_measurements(instance)
        representation['diseases'] = self.get_diseases(instance)
        representation['diet'] = self.get_diet(instance)
        return representation