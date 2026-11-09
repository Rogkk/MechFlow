from django.db import models

# Create your models here.
class ParticipanteModel(models.Model):
    nome_razao_social = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20) # decidir se tem que ser obrigatório

    TIPO_PESSOA_CHOICES = [
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]

    tipo_pessoa = models.CharField(max_length=1, choices=TIPO_PESSOA_CHOICES)
    nome_fantasia = models.CharField(max_length=100, null=True, blank=True) # só obrigatório para pessoa jurídica
    celular = models.CharField(max_length=20, null=True, blank=True)
    fone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    inscricao_estadual = models.CharField(max_length=20, null=True, blank=True) # só obrigatório para pessoa jurídica
    eh_contribuinte = models.BooleanField(default=False) # só obrigatório para pessoa jurídica
    inscricao_municipal = models.CharField(max_length=20, null=True, blank=True) # só obrigatório para pessoa jurídica
    eh_cliente = models.BooleanField(default=False)
    eh_fornecedor = models.BooleanField(default=False)
    eh_funcionario = models.BooleanField(default=False)
    empresa_id = models.IntegerField(null=True, blank=True) # id da empresa que o participante pertence
    criado_em = models.DateTimeField(auto_now_add=True) # ja registra a data na criação
    atualizado_em = models.DateTimeField(auto_now=True) # atualiza a data sempre que o registro for alterado
    criado_por = models.IntegerField(null=True, blank=True) # id do usuário que criou o registro
    
    def __str__(self):
            return self.nome_razao_social