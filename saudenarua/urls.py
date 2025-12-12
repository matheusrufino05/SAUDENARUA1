# Arquivo: saudenarua/urls.py
from django.urls import path
from ..saudenarua import views

urlpatterns = [
    # Página Inicial (Index)
    path('', views.index, name='index'),

    # Autenticação
    path('login/', views.login_view, name='login'),

    # Funcionalidades Principais
    path('mapa/', views.map_view, name='mapa'),
    path('medicamentos/', views.medicamentos_list, name='medicamentos_list'),
    path('relatos/', views.relatos_list, name='relatos_list'),

    # Rotas da API JWT
    path('api/login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]
