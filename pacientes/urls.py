from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import editar_paciente, listar_pacientes, confirmar_exclusao_paciente, cadastrar_paciente, excluir_paciente
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("cadastrar/", views.cadastrar_paciente, name="cadastrar_paciente"),
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/editar/<int:paciente_id>/', editar_paciente, name='editar_paciente'),  # URL para edição
    path("paciente/<int:pk>/", views.detalhes_paciente, name="detalhes_paciente"),
    path("paciente/<int:pk>/upload/", views.upload_arquivo, name="upload_arquivo"),
    path('pacientes/<int:pk>/arquivo/<int:arquivo_pk>/excluir/', views.excluir_arquivo, name='excluir_arquivo'),
    path('', listar_pacientes, name='listar_pacientes'),
    path('cadastrar/', cadastrar_paciente, name='cadastrar_paciente'),
    path('excluir/<int:paciente_id>/', excluir_paciente, name='excluir_paciente'),  # URL para excluir paciente
    path('confirmar_exclusao/<int:paciente_id>/', confirmar_exclusao_paciente, name='confirmar_exclusao_paciente'), #URL para Excluir paciente
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pacientes/', listar_pacientes, name='listar_pacientes'),  # URL para a lista de pacientes
    path("cadastro/", views.cadastro, name="cadastro"), # URL de cadastro de novos usuários
]

if settings.DEBUG:  # Apenas para desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)