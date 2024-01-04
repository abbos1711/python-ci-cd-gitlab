from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Main
from .serializers import MainModelSerializer


class CreateListMediaAPIView(generics.ListCreateAPIView, GenericViewSet):
    queryset = Main.objects.all()
    serializer_class = MainModelSerializer
    parser_classes = (FormParser, MultiPartParser)


class TopicRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView, GenericViewSet):
    queryset = Main.objects.all()
    serializer_class = MainModelSerializer


class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})