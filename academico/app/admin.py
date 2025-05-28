from django.contrib import admin
from .models import *

# Registros simples
admin.site.register(Cidade)
admin.site.register(Turnos)
admin.site.register(AvaliacaoTipo)
admin.site.register(Matricula)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(Avaliacao)
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
    inlines = [CursoInline]

admin.site.register(AreaSaber, AreaSaberAdmin)

class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [DisciplinaInline]

admin.site.register(Curso, CursoAdmin)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'turno')
    search_fields = ('nome',)
    list_filter = ('curso', 'turno')

admin.site.register(Turma, TurmaAdmin)

# ✅ Adicionando Pessoa ao admin

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cidade', 'ocupacao', 'turma')
    search_fields = ('nome', 'cpf')
    list_filter = ('cidade', 'ocupacao', 'turma')

admin.site.register(Pessoa, PessoaAdmin)

# Registrando Avaliacao (com ModelAdmin básico)


