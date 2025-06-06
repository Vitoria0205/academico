from django.contrib import admin
from .models import *

# Registros simples
admin.site.register(Cidade)
admin.site.register(Turnos)
admin.site.register(AvaliacaoTipo)
admin.site.register(Matricula)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(Disciplina)
admin.site.register(Frequencia)

# Inlines e ModelAdmins customizados
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaInline]

admin.site.register(Ocupacao, OcupacaoAdmin)

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]

admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(AreaSaber, AreaSaberAdmin)

class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_saber', 'instituicao_ensino')
    search_fields = ('nome',)
    list_filter = ('area_saber', 'instituicao_ensino')
    inlines = [DisciplinaInline]

admin.site.register(Curso, CursoAdmin)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'turno')
    search_fields = ('nome',)
    list_filter = ('curso', 'turno')

admin.site.register(Turma, TurmaAdmin)

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cidade', 'ocupacao', 'turma')
    search_fields = ('nome', 'cpf')
    list_filter = ('cidade', 'ocupacao', 'turma')

admin.site.register(Pessoa, PessoaAdmin)

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'curso', 'disciplina', 'avaliacao_tipo')
    search_fields = ('descricao', 'curso__nome', 'disciplina__nome', 'avaliacao_tipo__nome')
    list_filter = ('curso', 'disciplina', 'avaliacao_tipo')

admin.site.register(Avaliacao, AvaliacaoAdmin)

class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'curso', 'disciplina', 'numero_faltas')
    search_fields = ('pessoa__nome', 'curso__nome', 'disciplina__nome')
    list_filter = ('curso', 'disciplina')

admin.site.unregister(Frequencia)
admin.site.register(Frequencia, FrequenciaAdmin)

class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data', 'pessoa', 'curso', 'disciplina')
    search_fields = ('descricao', 'pessoa__nome', 'curso__nome', 'disciplina__nome')
    list_filter = ('curso', 'disciplina', 'data')

admin.site.unregister(Ocorrencia)
admin.site.register(Ocorrencia, OcorrenciaAdmin)

class CursoDisciplinaAdmin(admin.ModelAdmin):
    list_display = ('curso', 'disciplina', 'carga_horaria', 'periodo')
    search_fields = ('curso__nome', 'disciplina__nome')

admin.site.unregister(CursoDisciplina)
admin.site.register(CursoDisciplina, CursoDisciplinaAdmin)
