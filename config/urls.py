from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView,
    OcupacoesView,
    CidadesView,
    AreasSaberesView,
    TurmasView,
    TurnosView,
    AvaliacaoTiposView,
    PessoasView,
    InstituicoesEnsinosView,
    CursosView,
    DisciplinasView,
    MatriculasView,
    AvaliacoesView,
    FrequenciasView,
    OcorrenciasView,
    CursosDisciplinasView,
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('Ocupacao/', OcupacoesView.as_view(), name='Ocupacao'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('AreaSaber/', AreasSaberesView.as_view(), name='AreaSaber'),
    path('Turma/', TurmasView.as_view(), name='Turma'),
    path('Turnos/', TurnosView.as_view(), name='Turnos'),
    path('AvaliacaoTipo/', AvaliacaoTiposView.as_view(), name='AvaliacaoTipo'),
    path('Pessoa/', PessoasView.as_view(), name='pessoa'),
    path('InstituicaoEnsino/', InstituicoesEnsinosView.as_view(), name='InstituicaoEnsino'),
    path('Curso/', CursosView.as_view(), name='Curso'),
    path('Disciplina/', DisciplinasView.as_view(), name='Disciplina'),
    path('Matricula/', MatriculasView.as_view(), name='Matricula'),
    path('Avaliacao/', AvaliacoesView.as_view(), name='Avaliacao'),
    path('Frequencia/', FrequenciasView.as_view(), name='Frequencia'),
    path('Ocorrencia/', OcorrenciasView.as_view(), name='Ocorrencia'),
    path('CursoDisciplina/', CursosDisciplinasView.as_view(), name='CursoDisciplina'),
]
