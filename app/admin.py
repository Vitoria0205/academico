from django.contrib import admin
from .models import *
from django.contrib import admin

admin.site.register(Ocupacao)
admin.site.register(Cidade)
admin.site.register(AreaSaber)
admin.site.register(Turma)
admin.site.register(Turnos)
admin.site.register(AvaliacaoTipo)
admin.site.register(Pessoa)
admin.site.register(InstituicaoEnsino)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1 # Número de livros adicionais para adicionar no admin
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)# Campos que serão exibidos na listagem
    search_fields = ('nome',)# Campos que serão pesquisados
    inlines=[PessoaInline]

admin.site.register(Pessoa)
admin.site.register(Ocupacao,OcupacaoAdmin)


class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]

admin.site.register(Curso)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

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

admin.site.register(Disciplina)
admin.site.register(Curso, CursoAdmin)

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [AvaliacaoInline]

admin.site.register(Avaliacao)
admin.site.register(Disciplina, DisciplinaAdmin)

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaInline]

admin.site.register(Pessoa)
admin.site.register(Turma, TurmaAdmin)


class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [FrequenciaInline]

# Avaliações como Inline dentro de Disciplina
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [AvaliacaoInline]

# Registro final
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)



