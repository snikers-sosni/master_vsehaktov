from .import views
from django.urls import path
from .views import LoginView, RegistrationView, ProfileView

urlpatterns = [
    path('', views.index),
    path('login/', LoginView.as_view(), name='Login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile')
]