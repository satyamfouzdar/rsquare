from django.urls import path, include
from .views import dashboard, register

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', register, name='signup'),
]
