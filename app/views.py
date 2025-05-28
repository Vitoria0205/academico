from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
class IndexView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'index.html', {'pessoas': pessoas})
    

class OcupacoesView(View):
    def get(self, request, *args,**kwargs):
        ocupacoes=Ocupacao.objects.all()
        return render(request, "ocupacao.html",{"ocupacoes":ocupacoes})


class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class AreasSaberesView(View):
    def get(self, request, *args, **kwargs):
        areassaberes = AreaSaber.objects.all()
        return render(request, 'areasaber.html', {'areassaberes': areassaberes})
    

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turnos.objects.all()
        return render(request, 'turnos.html', {'turnos': turnos})

class AvaliacaoTiposView(View):
    def get(self, request, *args, **kwargs):
        avaliacaotipos = AvaliacaoTipo.objects.all()
        return render(request, 'avaliacaotipo.html', {'avaliacaotipos': avaliacaotipos})

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class InstituicoesEnsinosView(View):
    def get(self, request, *args, **kwargs):
        instituicoesensinos = InstituicaoEnsino.objects.all()
        return render(request, 'instituicaoensino.html', {'instituicoesensinos': instituicoesensinos})

class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas': disciplinas})

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes': avaliacoes})
    
class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias': frequencias})
    
class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias': ocorrencias})

class CursosDisciplinasView(View):
    def get(self, request, *args, **kwargs):
        cursosdisciplinas = CursoDisciplina.objects.all()
        return render(request, 'cursodisciplina.html', {'cursosdisciplinas': cursosdisciplinas})

# class DeletePessoaView(View):
#     def get(self, request, id, *args, **kwargs):
#         pessoa= Pessoa.objects.get(id=id)
#         pessoa.delete()
#         messages.success(request, 'Excluído com sucesso!') # Success message
#         return redirect('pessoas')
    
# class EditarPessoaView(View):
#     template_name = 'editar_pessoa.html'
#     def get(self, request, id, *args, **kwargs):
#         pessoa = get_object_or_404(Pessoa, id=id)
#         form = PessoaForm(instance=pessoa)
#         return render(request, self.template_name, {'pessoa': pessoa,'form': form})
#     def post(self, request, id, *args, **kwargs):
#         pessoa = get_object_or_404(Pessoa, id=id)
#         form = PessoaForm(request.POST, instance=pessoa)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'As edições foram salvas com sucesso.')
#             return redirect('editar', id=id) # Redirecionar de volta para a página de edição
#         else:
#             messages.error(request, 'Corrija os erros no formulário antes de enviar novamente.')
#         return render(request, self.template_name, {'pessoa': pessoa,'form': form})
