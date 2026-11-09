from django import forms
from .models import ParticipanteModel

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = ParticipanteModel
        fields = [
            'nome_razao_social',
            'cpf_cnpj',
            'tipo_pessoa',
            'nome_fantasia',
            'celular',
            'fone',
            'email',
            'cep',
            'endereco',
            'numero',
            'complemento',
            'bairro',
            'cidade',
            'uf',
            'inscricao_estadual',
            'eh_contribuinte',
            'inscricao_municipal',
            'eh_cliente',
            'eh_fornecedor',
            'eh_funcionario',
            'empresa_id'
        ]

        