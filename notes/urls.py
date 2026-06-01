from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
from django.urls import path,include

router=DefaultRouter()
router.register('notes',NoteViewSet)
urlpatterns=[path('',include(router.urls)),]