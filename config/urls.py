"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacao'),
    path('cidade', CidadesView.as_view(), name='cidade'),
    path('areasaber/', AreasSaberesView.as_view(), name='areasaber'),
    path('turma/', TurmasView.as_view(), name='turma'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('avaliacaotipo/', AvaliacaoTiposView.as_view(), name='avaliacaotipo'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('instituicaoensino', InstituicoesEnsinosView.as_view(), name='instituicaoensino'),
    path('curso/', CursosView.as_view(), name='cursos'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
    path('avaliacao/', AvaliacoesView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciasView.as_view(), name='frquencia'),
    path('ocorrencia/', OcorrenciasView.as_view(), name='ocorrencia'),
    path('cursodisciplina', CursosDisciplinasView.as_view(), name='cursodisciplina'),
    path('delete/<int:id>/', DeletePessoaView.as_view(),name='delete'),
]

