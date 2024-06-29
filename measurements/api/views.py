from rest_framework import generics, status
from measurements.models import BodyMeasurement, SegmentalBodyMeasurement, BiochemicalMeasurement, Diseases, Diet
from measurements.api.serializers import *
from rest_framework.response import Response
from .permissions import IsOwner, IsNutritionistClientOwner

"""
All the APIViews have overriden get_queryset and create methods to support the access 
for both NormalUsers and Nutritionists end points.

The create method sets either the user field or the client field to null depending on the endpoint.
"""

class GenericQuerysetMixin:
    """
    Mixin that provies a generic get_queryset method for all the measurement models.
    """
    def generic_queryset(self, model):
        if 'user_pk' in self.kwargs:
            return model.objects.filter(user_id=self.kwargs['user_pk'])
        elif 'nutritionist_pk' in self.kwargs and 'client_pk' in self.kwargs:
            return model.objects.filter(client_id=self.kwargs['client_pk'])
        else:
            return model.objects.none()

class BaseMeasurementDetailAPIView(GenericQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    Base class for all the measurement detail views.
    Provides a generic update method for all the measurement models.
    """

    def get_permissions(self):
        """
        This method sets the permissions based on the endpoint.
        """
        if 'user_pk' in self.kwargs:
            self.permission_classes = [IsOwner]
        else:
            self.permission_classes = [IsNutritionistClientOwner]
        return super().get_permissions()

    def get_queryset(self):
        return self.generic_queryset(self.model)
    
    def update(self, request, *args, **kwargs):
        """
        This update method prevents the update of the user, client and nutritionist fields.
        """
        instance = self.get_object()
        partial = kwargs.pop('partial', False)
        data = request.data.copy()
        data.pop('user', None)
        data.pop('client', None)
        if partial:
            data.pop('nutritionist', None)
        elif 'nutritionist' in data:
            data['nutritionist'] = instance.nutritionist.id # Prevents the nutritionist field from being updated.

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class BaseMeasurementListCreateAPIView(GenericQuerysetMixin, generics.ListCreateAPIView):
    """
    Base class for all the measurement list and create views.
    Provides a generic create methods for all the measurement models.
    """

    def get_permissions(self):
        """
        This method sets the permissions based on the endpoint.
        """
        if 'user_pk' in self.kwargs:
            self.permission_classes = [IsOwner]
        else:
            self.permission_classes = [IsNutritionistClientOwner]
        return super().get_permissions()

    def get_queryset(self):
        return self.generic_queryset(self.model)
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = kwargs.get('user_pk')
        data['client'] = kwargs.get('client_pk')
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class AllClientMeasurementsView(generics.GenericAPIView):
    """
    This view returns all the measurements associated with a client.
    """
    permission_classes = [IsNutritionistClientOwner]

    def get(self, request, *args, **kwargs):
        client_pk = kwargs.get('client_pk')
        serializer = AllClientMeasurementsSerializer(context={'client_pk': client_pk})
        data = serializer.to_representation(None)
        return Response(data, status=status.HTTP_200_OK)

class AllUserMeasurementsView(generics.GenericAPIView):
    """
    This view returns all the measurements associated with a user.
    """
    permission_classes = [IsOwner]

    def get(self, request, *args, **kwargs):
        user_pk = kwargs.get('user_pk')
        serializer = AllUserMeasurementsSerializer(context={'user_pk': user_pk})
        data = serializer.to_representation(None)
        return Response(data, status=status.HTTP_200_OK)
    
class BodyMeasurementListCreateAPIView(BaseMeasurementListCreateAPIView):
    serializer_class = BodyMeasurementSerializer
    model = BodyMeasurement

class BodyMeasurementDetailAPIView(BaseMeasurementDetailAPIView):
    serializer_class = BodyMeasurementSerializer
    model = BodyMeasurement

class SegmentalBodyMeasurementListCreateAPIView(BaseMeasurementListCreateAPIView):
    serializer_class = SegmentalBodyMeasurementSerializer
    model = SegmentalBodyMeasurement

class SegmentalBodyMeasurementDetailAPIView(BaseMeasurementDetailAPIView):

    serializer_class = SegmentalBodyMeasurementSerializer
    model = SegmentalBodyMeasurement

class BiochemicalMeasurementListCreateAPIView(BaseMeasurementListCreateAPIView):
    serializer_class = BiochemicalMeasurementSerializer
    model = BiochemicalMeasurement

class BiochemicalMeasurementDetailAPIView(BaseMeasurementDetailAPIView):
    serializer_class = BiochemicalMeasurementSerializer
    model = BiochemicalMeasurement

class DiseasesListCreateAPIView(BaseMeasurementListCreateAPIView):
    serializer_class = DiseasesSerializer
    model = Diseases

class DiseasesDetailAPIView(BaseMeasurementDetailAPIView):
    serializer_class = DiseasesSerializer
    model = Diseases

class DietListCreateAPIView(BaseMeasurementListCreateAPIView):
    serializer_class = DietSerializer
    model = Diet

    def create(self, request, *args, **kwargs):
        """
        This create method is overriden to also handle the nutritionist field.
        """
        data = request.data.copy()
        data['user'] = kwargs.get('user_pk')
        data['client'] = kwargs.get('client_pk')
        data['nutritionist'] = kwargs.get('nutritionist_pk')
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DietDetailAPIView(BaseMeasurementDetailAPIView):
    serializer_class = DietSerializer
    model = Diet
