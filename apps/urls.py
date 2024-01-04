from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateListMediaAPIView, TopicRetrieveDestroyAPIView, HelloWorldAPIView

router = DefaultRouter()
router.register(r'add_media', CreateListMediaAPIView, basename='add')
router.register(r'remove_media', TopicRetrieveDestroyAPIView, basename='remove')

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', HelloWorldAPIView.as_view())
]
