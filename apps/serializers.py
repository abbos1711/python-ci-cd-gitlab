from rest_framework.serializers import ModelSerializer

from apps.models import Main


class MainModelSerializer(ModelSerializer):
    class Meta:
        model = Main
        fields = ['image', 'video']


class MainRemoveModelSerializer(ModelSerializer):
    class Meta:
        model = Main
        fields = ['image', 'video']
