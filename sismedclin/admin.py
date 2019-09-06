from material.admin.options import MaterialModelAdmin
from django.contrib import admin
from material.admin.sites import site

from.models import Paciente,Convenio,Medico,Agendamento,Receita,Financeiro,Resultado,Prontuario


class PacienteAdmin(MaterialModelAdmin):
    list_display = ('Nome', 'Cpf', 'Telefone','Celular','Email')
    icon_name = 'assignment_ind'
    list_filter = ('Nome',)
    search_fields = ('Nome,','Cpf')

   
    
class ConvenioAdmin(MaterialModelAdmin):
    list_display = ('Nome', 'Registro_ANS', 'Tipo')  
    icon_name = 'business_center'  

class ReceitaInline(admin.TabularInline):
    model = Receita
    extra = 0
    
class MedicoAdmin(MaterialModelAdmin):
    list_display = ('codigo','Nome', 'Crm', 'Especialidade',)  
    readonly_fields = ('codigo',)
    icon_name = 'enhanced_encryption'  
    list_filter = ('Nome',)
    search_fields = ('Nome,','Crm')
    inlines = [ReceitaInline]

class AgendamentoAdmin(MaterialModelAdmin):
    list_display = ('Paciente', 'Data', 'Telefone','Especialidade','Medico','Status')  
    icon_name = 'access_time'
    list_filter = ('Data',)
    search_fields = ('Nome,','Data')
     

class ReceitaAdmin(MaterialModelAdmin):
    list_display = ('Paciente', 'Numero_receita', 'Data_receita','Medicamento','Medico')  
    readonly_fields = ('Numero_receita',)
    icon_name = 'assignment'
    
class FinanceiroAdmin(MaterialModelAdmin):
    list_display = ('Paciente', 'Data_vencimento', 'Data_pagamento','Valor','Status','Operacao','descricao')  
    icon_name = 'credit_card'
    list_filter = ('Status',)
    search_fields = ('Status,','Data_vencimento')

class ResultadoAdmin(MaterialModelAdmin):
    list_display = ('Paciente', 'Data', 'Medico')  
    icon_name = 'assignment_turned_in'
    list_filter = ('Paciente','Data')
    search_fields = ('Paciente,',)
    
class ProntuarioAdmin(MaterialModelAdmin):
    list_display = ('Numero', 'Data_abertura', 'Paciente','Medico')  
    icon_name = 'content_paste'
    list_filter = ('Paciente',)
    search_fields = ('Paciente,','Numero')
    
site.register(Paciente,PacienteAdmin)
site.register(Convenio,ConvenioAdmin)
site.register(Medico,MedicoAdmin)
site.register(Agendamento,AgendamentoAdmin)
site.register(Receita,ReceitaAdmin)
site.register(Financeiro,FinanceiroAdmin)
site.register(Resultado,ResultadoAdmin)
site.register(Prontuario,ProntuarioAdmin)