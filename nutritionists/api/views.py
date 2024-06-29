from rest_framework import generics, status
from nutritionists.models import Nutritionist
from users.models import NormalUser, CustomUser
from rest_framework.response import Response
from nutritionists.api.serializers import *
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from nutritionists.api.permissions import IsNutritionistOwner, IsNutritionistClientOwner

class NutritionistListAPIView(generics.ListCreateAPIView):
    """
    Standard ListCreateAPIView for Nutritionist model accessible only for staff users.
    """
    queryset = Nutritionist.objects.all()
    serializer_class = NutritionistSerializer
    
    permission_classes = [IsAdminUser]

class NutritionistDetailAPIView(generics.RetrieveUpdateAPIView):
    """
    This view handles the retrieval and update of a Nutritionist instance.
    Delete method is not implemented as it is handled by CASCADE during the deletion of the related CustomUser.
    """
    queryset = Nutritionist.objects.all()
    serializer_class = NutritionistSerializer
    permission_classes = [IsNutritionistOwner or IsAdminUser]

class NutritionistClientListCreateAPIView(generics.ListAPIView):
    """
    This view handles the retrieval and creation of a list of Clients related to the authenticated Nutritionist.
    Overriding the methods of the APIView is necessary so that both GET and POST requests can be handled from a single endpoint.
    """
    permission_classes = [IsNutritionistClientOwner or IsAdminUser]

    def get_serializer_class(self):
        return ClientListSerializer if self.request.method == 'GET' else ClientCreateSerializer

    def get_queryset(self):
        nutritionist_pk = self.kwargs['nutritionist_pk']
        nutritionist = get_object_or_404(Nutritionist, pk=nutritionist_pk)
        return nutritionist.clients.all()
    
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NutritionistClientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view handles the Retrieve, Update and Destroy operations of a Client instance related to the authenticated Nutritionist.
    """
    serializer_class = ClientCreateSerializer
    permission_classes = [IsNutritionistClientOwner]

    def get_queryset(self):
        nutritionist = get_object_or_404(Nutritionist, id=self.kwargs['nutritionist_pk'])
        return nutritionist.clients.all()

    def get_object(self):
        client = get_object_or_404(self.get_queryset(), id=self.kwargs['client_pk'])
        return client

class UserToClientLinkAPIView(generics.UpdateAPIView):
    """
    This view is used to link an existing NormalUser to a Client.
    Only basic information data are linked to the Client.
    """
    # To be implemented - Due to security and personal privacy reasons,
    # confirmation from the user is required before linking the user to a client
    queryset = NormalUser.objects.all()
    serializer_class = UserToClientLinkSerializer
    permission_classes = [IsNutritionistClientOwner]

    def get_object(self):
        client = get_object_or_404(self.queryset, id=self.kwargs['client_pk'])
        return client
    
    # Since only existing NormalUsers can be linked to a Client, no request data are required
    # and the NormalUser can be fetched directly from the database
    def get_serializer_context(self):
        context = super().get_serializer_context()
        user_id = self.kwargs.get('user_pk')
        if user_id is not None:
            user = get_object_or_404(CustomUser, id=user_id)
            context['user'] = user
        return context
    
    def update(self, request, *args, **kwargs):
        partial = True  # Only partial update is supported
        instance = self.get_object()
        data = request.data.copy() # Empty data, used to meet requirements for serializer.is_valid() only
        context=self.get_serializer_context()

        serializer = self.get_serializer(instance, data=data, partial=partial, context=context)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)