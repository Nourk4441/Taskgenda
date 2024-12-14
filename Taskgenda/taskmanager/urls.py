from django.urls import path
from . import views
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('api-token-auth/', drf_views.obtain_auth_token, name='api-token-auth'),
]