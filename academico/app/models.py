from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome: ")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Area")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "AreaSaber"
        verbose_name_plural = "AreasSaberes"

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Turma")
    periodo = models.CharField(max_length=100, verbose_name="Periodo", default=1)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, verbose_name="Curso: ", default=1)
    turno = models.ForeignKey('Turnos', on_delete=models.CASCADE, verbose_name="Turno: ", default=1)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Turnos(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Turno")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de Avaliação")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "AvaliacaoTipo"
        verbose_name_plural = "AvaliacaoTipos"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Pessoa:")
    pai = models.CharField(max_length=100, verbose_name="Nome do Pai:")
    mae = models.CharField(max_length=100, verbose_name="Nome da Mãe:")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name='Data de nascimento: ')
    email = models.EmailField(verbose_name="Email: ")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade: ")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação: ")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, default=1)

    
    def __str__(self):
        return f"{self.nome} ({self.cidade})"
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição de Ensino:")
    site = models.CharField(max_length=100, verbose_name="Site:")
    telefone = models.CharField(max_length=100, verbose_name="Telefone:")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade: ")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "InstituicaoEnsino"
        verbose_name_plural = "InstituicoesEnsinos"

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso:")
    carga_horaria_total = models.CharField(max_length=100, verbose_name="Carga Horária:")
    duracao_meses = models.CharField(max_length=100, verbose_name="Duração em meses:")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="AreaSaber: ")
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituicao de Ensino: ")
    
    
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina:")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="AreaSaber: ")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituicao de Ensino: ")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso: ")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa: ")
    data_inicio = models.DateField(verbose_name='Data de Inicio: ')
    data_previsao_termino = models.DateField(verbose_name='Data de previsão de término do curso: ')
    
    def __str__(self):
        return f"Instituição: {self.instituicao_ensino}, Curso: {self.curso}, Pessoa: {self.pessoa}, Data de início: {self.data_inicio}, Data de previsão de término: {self.data_previsao_termino}"
    
    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição :")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso: ")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina: ")
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo de avaliação: ", default=1)
    
    def __str__(self):
        return f"{self.avaliacao_tipo} de {self.disciplina}"
    
    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso: ")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina: ")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa: ")
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas :")
    
    def __str__(self):
        return f"{self.pessoa}, faltou na disciplina {self.disciplina} e a quantidade do número de faltas é {self.numero_faltas}"
    
    class Meta:
        verbose_name = "Frequencia"
        verbose_name_plural = "Frequencias"

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição :")
    data = models.DateField(verbose_name="Data :")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso: ")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina: ")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa: ")
    
    def __str__(self):
        return f"{self.pessoa}, {self.descricao} na aula {self.disciplina} na data tal {self.data}"
    
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina: ")
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga Horária :")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso: ")
    periodo = models.CharField(max_length=100, verbose_name="Período :")
    
    def __str__(self):
        return f"{self.curso} com as disciplinas {self.disciplina}"
    
    class Meta:
        verbose_name = "CursoDisciplina"
        verbose_name_plural = "CursoDisciplinas"
