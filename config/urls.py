# Arquivo: saudenarua/urls.py
from django.contrib import admin
from django.urls import path, include
from ..saudenarua import views

urlpatterns = [
    # Rota Administrativa
    path('admin/', admin.site.urls),
    path('', include('saudenarua.urls')),
]
