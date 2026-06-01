from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet

urlpatterns=[
    path("users/",views.show_users),
    path('add/',views.add_user),
    path('signup/',views.signup),
    path('login/',views.login_user),
    path("logout/", views.logout_user),
    path("form/", views.form_page)
]

router=DefaultRouter()
router.register('ToDo',ToDoViewSet)

urlpatterns+=router.urls