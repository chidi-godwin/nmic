from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Register.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('', views.Index.as_view(), name='index')
]