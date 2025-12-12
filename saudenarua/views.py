# Arquivo: saudenarua/views.py
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

# View da Página Inicial
def index(request):
    return render(request, 'index.html')

# View para Login (apenas renderiza o template por enquanto)
def login_view(request):
    return render(request, 'login.html')

# View do Mapa
def map_view(request):
    # Dados fictícios para o mapa funcionar
    farmacias = [
        {'lat': -8.063149, 'lng': -34.871139, 'nome': 'Farmácia Central'},
        {'lat': -8.050000, 'lng': -34.900000, 'nome': 'UBS Centro'}
    ]
    return render(request, 'map.html', {'farmacias': farmacias})

# View de Medicamentos
def medicamentos_list(request):
    lista_medicamentos = [
        {'nome': 'Dipirona 500mg', 'codigo': '12345'},
        {'nome': 'Paracetamol 750mg', 'codigo': '67890'},
    ]
    return render(request, 'medicamentos/medicamentos_list.html', {'medicamentos': lista_medicamentos})

# View de Estoque
def estoque_list(request):
    estoque = [
        {'estabelecimento': 'Farmácia A', 'medicamento': 'Amoxicilina', 'quantidade': 10},
    ]
    return render(request, 'estoque/estoque_list.html', {'estoque': estoque})

# View de Estabelecimentos
def estabelecimentos_list(request):
    estabelecimentos = [
        {'id': 1, 'nome': 'UBS Santo Amaro', 'tipo': 'UBS', 'endereco': 'Rua da Aurora'},
    ]
    return render(request, 'estabelecimentos/listar.html', {'estabelecimentos': estabelecimentos})

# View de Relatos
def relatos_list(request):
    relatos = [
        {'estabelecimento': 'UPA Caxangá', 'descricao': 'Bom atendimento', 'tempo_espera': 30},
    ]
    return render(request, 'relatos/relatos_list.html', {'relatos': relatos})

def medicamento_create(request):
    return render(request, 'medicamento_form.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")  # coloque o nome da URL da sua página inicial

        return render(request, "login.html", {
            "error": "Usuário ou senha incorretos."
        })

    return render(request, "login.html")
