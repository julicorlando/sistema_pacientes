from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import adicionar_pagamento, detalhes_paciente, editar_paciente, excluir_pagamento, listar_pacientes, confirmar_exclusao_paciente, cadastrar_paciente, excluir_paciente
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("cadastrar/", views.cadastrar_paciente, name="cadastrar_paciente"),
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('pacientes/editar/<int:paciente_id>/', editar_paciente, name='editar_paciente'),  # URL para edição
    path('paciente/<int:pk>/', detalhes_paciente, name='detalhes_paciente'),
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
    path('paciente/<int:paciente_id>/registrar_pagamento/', views.registrar_pagamento, name='registrar_pagamento'),    #URL Registrar pagamento
    path('paciente/<int:pk>/', views.detalhes_paciente, name='detalhes_paciente'),
    path('paciente/<int:paciente_id>/adicionar_pagamento/', adicionar_pagamento, name='adicionar_pagamento'),
    path('pacientes/<int:paciente_id>/adicionar_pagamento/', views.adicionar_pagamento, name='adicionar_pagamento'),
    path('pacientes/paciente/<int:pk>/', detalhes_paciente, name='detalhes_paciente'),
    path('pacientes/paciente/<int:paciente_id>/excluir_pagamento/<int:pagamento_id>/', excluir_pagamento, name='excluir_pagamento'),
    path('paciente/<int:paciente_id>/evolucoes/', views.evolucoes, name='evolucoes'),
    path('paciente/<int:paciente_id>/adicionar_evolucao/', views.adicionar_evolucao, name='adicionar_evolucao'),
    path('evolucao/editar/<int:id>/', views.editar_evolucao, name='editar_evolucao'),
    path('evolucao/<int:evolucao_id>/excluir/', views.excluir_evolucao, name='excluir_evolucao'),
    path('paciente/<int:pk>/', detalhes_paciente, name='detalhes_paciente'),
    path('pacientes/evolucao/editar/<int:evolucao_id>/', views.editar_evolucao, name='editar_evolucao'),
    path('pacientes/detalhes/<int:paciente_id>/', views.detalhes_paciente, name='detalhes_pacientes'),
    path('pacientes/paciente/<int:paciente_id>/', views.detalhes_paciente, name='detalhes_paciente'),
]
if settings.DEBUG:  # Apenas para desenvolvimento
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)