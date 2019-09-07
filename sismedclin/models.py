from django.db import models
from django.db.models import Sum


class Paciente(models.Model):
    CIVIL_CHOICES = (
        ('S', 'SOLTEIRO'),
        ('C', 'CASADO'),
        ('D', 'DIVORCIADO'),
        ('O', 'OUTROS'),
        
    )
    SEXO_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMININO'),
        ('HT', 'HOMEM TRANS'),
        ('MT', 'MULHER TRANS'),    
    )
    PNE_CHOICES = (
        ('S', 'SIM'),
        ('N', 'NÃO'),
    )
    ESTADO_CHOICES= (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    
    Data_criacao = models.DateField()
    Nome = models.CharField(max_length=100)
    Data_nascimento = models.DateField()
    Naturalidade = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    Cpf = models.CharField(max_length=14, unique=True)
    Rg = models.CharField(max_length=8, unique=True)
    Orgao_emissor = models.CharField(max_length=10)
    Sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    Telefone = models.CharField(max_length=15)
    Celular = models.CharField(max_length=15)
    Email = models.EmailField(blank=True, null=True)
    Cep = models.CharField(max_length=10)
    Endereco = models.CharField(max_length=100)
    Numero_casa = models.CharField(max_length=10)
    Bairro = models.CharField(max_length=40)
    Cidade = models.CharField(max_length=100)
    Estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    Profissao = models.CharField(max_length=50, blank=True, null=True)
    Estado_civil = models.CharField(max_length=1, choices=CIVIL_CHOICES)
    Pai = models.CharField(max_length=100, blank=True, null=True)
    Mae = models.CharField(max_length=100)
    Pne = models.CharField(max_length=1, choices=PNE_CHOICES)
    Tipo_sanguineo = models.CharField(max_length=4)
    Observacoes = models.TextField(blank=True, null=True)
    
    def __str__(self):            
        return self.Nome

    
class Convenio(models.Model):
    TIPO_CHOICES =(
        ('PP', 'PLANO PRIVADO'),
        ('PU', 'PLANO PUBLICO'),
        ('PA', 'PARTICULAR'),
        ('GT', 'GRATUITO'),
        ('FI', 'FINANCIADO PELO SUS'),
        ('DP', 'DPVAT'),
         
    )
    Nome = models.CharField(max_length=50)
    Registro_ANS = models.CharField(max_length=15)
    Tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    
    def __str__(self):
        return self.Nome

class Medico(models.Model):
    ESPECIALIDADE_CHOICES = (
        ('AL', 'Alergia_Imunologia'),
        ('AN', 'Angiologia'), 
        ('CA', 'Cardiologia'), 
        ('CM', 'Clínica_Médica'),
        ('DM', 'Dermatologia'), 
        ('EN', 'Endocrinologia'),
        ('ED', 'Endoscopia'),
        ('GS', 'Gastroenterologia'),
        ('GE', 'Geriatria'),
        ('GI', 'Ginecologia'),
        ('HE', 'Hematologia'),
        ('IF', 'Infectologia'),
        ('MA', 'Mastologia'),
        ('MT', 'Medicina_do_Trabalho'),
        ('NF', 'Nefrologia'),
        ('NE', 'Neurologia'),
        ('OF', 'Oftalmologia'),
        ('ON', 'Oncologia'),
        ('OR', 'Ortopedia'),
        ('OT', 'Otorrinolaringologia'),
        ('PE', 'Pediatria'),
        ('PN', 'Pneumologia'),
        ('PS', 'Psiquiatria'),
        ('RA', 'Radiologia'),
        ('RT', 'Radioterapia'),
        ('RE', 'Reumatologia'),
        ('UR', 'Urologia'),
        
    )
    codigo = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=50)
    Crm = models.CharField(max_length=14, unique=True)
    Rg = models.CharField(max_length=8, unique=True)
    Cpf = models.CharField(max_length=14, unique=True)
    Especialidade = models.CharField(max_length=2, choices=ESPECIALIDADE_CHOICES)
    
    def __str__(self):
        return self.Nome
        
class Agendamento(models.Model):
    ESPECIALIDADE_CHOICES = (
        ('AL', 'Alergia_Imunologia'),
        ('AN', 'Angiologia'), 
        ('CA', 'Cardiologia'), 
        ('CM', 'Clínica_Médica'),
        ('DM', 'Dermatologia'), 
        ('EN', 'Endocrinologia'),
        ('ED', 'Endoscopia'),
        ('GS', 'Gastroenterologia'),
        ('GE', 'Geriatria'),
        ('GI', 'Ginecologia'),
        ('HE', 'Hematologia'),
        ('IF', 'Infectologia'),
        ('MA', 'Mastologia'),
        ('MT', 'Medicina_do_Trabalho'),
        ('NF', 'Nefrologia'),
        ('NE', 'Neurologia'),
        ('OF', 'Oftalmologia'),
        ('ON', 'Oncologia'),
        ('OR', 'Ortopedia'),
        ('OT', 'Otorrinolaringologia'),
        ('PE', 'Pediatria'),
        ('PN', 'Pneumologia'),
        ('PS', 'Psiquiatria'),
        ('RA', 'Radiologia'),
        ('RT', 'Radioterapia'),
        ('RE', 'Reumatologia'),
        ('UR', 'Urologia'),
        
    )
    STATUS_CHOICES =(
        ('AG', 'AGENDADO'),
        ('AT', 'ATENDIDO'),
        ('CA', 'CANCELADO'),
        ('NC', 'NAO COMPARECEU'),
        
    )
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Data = models.DateField()
    Nascimento = models.DateField()
    Telefone = models.CharField(max_length=20)
    Especialidade = models.CharField(max_length=2, choices=ESPECIALIDADE_CHOICES)
    Unidade = models.CharField(max_length=40)
    Status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    Convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    Medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    Valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
 
    def __str_(self):
        return self.Paciente
    

class Receita(models.Model):
    Paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    Numero_receita = models.AutoField(primary_key=True)
    Medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    Data_receita = models.DateField(auto_now=True)
    Medicamento = models.CharField(max_length=100, blank=True, null=True)
    Posologia = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
         return str(self.Paciente)    
 
class Financeiro(models.Model):
    STATUS=(
        ('a', 'Apagar'),
        ('p', 'Pago'),       
    )
    TIPO_OPERACAO=(
        ('DE', 'Debito'),
        ('CR', 'Credito'),
        ('DI', 'Dinheiro'),
        
    )
     
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)
    Data_vencimento = models.DateField()
    Data_pagamento = models.DateField(null=True, blank=True)
    Valor = models.DecimalField(max_digits=15, decimal_places=2)
    Status = models.CharField(max_length=1, choices=STATUS)
    Operacao = models.CharField(max_length=2, choices=TIPO_OPERACAO,blank=True)
    descricao = models.TextField(blank=True)

    def total(self):
        Financeiro.objects.aggregate(total=Sum('Valor'))
    
class Resultado(models.Model):
    Paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    Imagem = models.FileField(upload_to='media',blank=True, null=True) 
    Data = models.DateField()
    Medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    Anotacoes = models.TextField(blank=True, null=True)
    Receitas = models.ForeignKey(Receita, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.Paciente)   
    
class Prontuario(models.Model):
    SEXO = (
        ('M', 'MASCULINO'),
        ('F', 'FEMININO'),
        ('HT', 'HOMEM TRANS'),
        ('MT', 'MULHER TRANS'),    
        
    )
    
    Numero = models.AutoField(verbose_name='Numero Prontuario',primary_key=True)
    Data_abertura = models.DateField(auto_now=True)
    Paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    Data_nascimento = models.DateField()
    Endereco = models.CharField(max_length=150, verbose_name='Endereço')
    Telefone = models.CharField(max_length=12)
    Sexo = models.CharField(max_length=2, choices=SEXO)
    Medico = models.ForeignKey(Medico, on_delete=models.PROTECT, blank=True, null=True)
    Alergia = models.CharField(max_length=5)
    Altura = models.DecimalField(max_digits=5, decimal_places=2)
    Peso = models.DecimalField(max_digits=10, decimal_places=5)
    Tipo_sanguineo = models.CharField(max_length=5, blank=True, null=True)
  
    
    def __str__(self):
        return str(self.Paciente)           