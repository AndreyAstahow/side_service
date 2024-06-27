from django.urls import path
from .views import BaseRegisterView, upgrade_me

urlpatterns = [
    path('sign/', BaseRegisterView.as_view(template_name = 'sign/sign.html'), name='signup'),
    path('upgrade/', upgrade_me, name='upgrade')
]