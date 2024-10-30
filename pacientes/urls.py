from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import editar_paciente, listar_pacientes, confirmar_exclusao_paciente, cadastrar_paciente, excluir_paciente

urlpatterns = [
    path('cadastrar/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/editar/<int:paciente_id>/', editar_paciente, name='editar_paciente'),  # URL para edição
    path('paciente/<int:paciente_id>/', views.detalhes_paciente, name='detalhes_paciente'),
    path('paciente/<int:paciente_id>/upload/', views.upload_arquivo, name='upload_arquivo'),
    path('arquivo/<int:arquivo_id>/excluir/', views.excluir_arquivo, name='excluir_arquivo'),
    path('', listar_pacientes, name='listar_pacientes'),
    path('cadastrar/', cadastrar_paciente, name='cadastrar_paciente'),
    path('excluir/<int:paciente_id>/', excluir_paciente, name='excluir_paciente'),  # URL para excluir paciente
    path('confirmar_exclusao/<int:paciente_id>/', confirmar_exclusao_paciente, name='confirmar_exclusao_paciente'), #URL para Excluir paciente
]

if settings.DEBUG:  # Apenas para desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)