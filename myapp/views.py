from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Client, Artist, Work
from .serializers import ClientSerializer, ArtistSerializer, WorkSerializer

class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['work_type']
    search_fields = ['artists__name']
    queryset = Work.objects.all()

class RegisterUser(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
