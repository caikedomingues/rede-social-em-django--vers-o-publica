
# Import da biblioteca models que possui os campos
# de criação de classes (colunas) no banco de 
# dados.
from django.db import models

# Import da classe User do django, que irá 
# conter os atributos básicos da criação de 
# um usuário como usernames e passwords  
from django.contrib.auth.models import User
# Create your models here.

# Vamos criar uma coluna que irá conter as contas registradas 
# na nossa rede social. Como o recomendável é usar a classe
# User na criação de usuários (por que a classe user criptografa
# senhas no banco de dados), vamos associar as contas um usuário
# que anteriormente foi criado no sistema. Na regra de criação de
# classes models, devemos passar como herança a classe Model da
# bilboteca models que irá conter os campos necessários para a
# a criação dos atributos da classe.
class conta(models.Model):
    
    # Ira conter o nome do criador da conta
    nome = models.CharField(max_length=400)
    
    # Ira conter a idade do criador da conta
    idade = models.IntegerField()
    
    # Ira conter uma breve biografia do criador da conta
    biografia = models.CharField(max_length=1000)
    
    # Ira conter uma breve descrição dos assuntos que 
    # criador da conta se interessa
    interesses = models.CharField(max_length=1000)
    
    # Ira xonter o estado civil do usuário
    estado_civil = models.CharField(max_length=500)
    
    # Vamos criar uma chave estrangeira que irá relacionar o usuário 
    # a conta criada na rede, com o objetivo de atribuir um dono a
    # conta
    dono_da_conta = models.ForeignKey(User,  on_delete=models.CASCADE)
    
    # Coluna que irá conter todas as contas que seguem o usuário
    # na nossa rede social. Nesse caso como um conta ou mais podem
    # seguir o usuário, temos uma relação de banco de dados do tipo
    # muito para muitos.
    
    # ManyToManyField: Isso diz ao Django que o campo seguidores no
    # nosso modelo Conta representa um relacionamento do tipo muitos-para-
    # muitos com outro modelo. Em termos simples, uma conta pode estar
    # relacionada a muitas outras contas (como nesse caso, onde temos
    # as contas que nos seguem), e muitas outras contas podem estar 
    # relacionada a  muitas outras contas(como as contas que ela segue).
    
    # self:  Essa palavra especial significa que o relacionamento 
    # muitos-para-muitos é com o próprio modelo Conta. Ou seja, uma
    # Conta se relaciona com outras contas. É como se a tabela de
    # contas estivesse se relacionando consigo mesma para definir
    # quem segue quem.  
    
    # Symmetrical: Essa opção controla se o relacionamento
    # é considerado simétrico ou não. 
    
    # False: Ao definir como False, estamos dizendo que a relação
    # de "seguir" não é automática nos dois sentidos, ou seja, se
    # a conta A segue a conta B, isso não significa que automaticamente
    # que a conta B segue a conta A. É uma relação direcionada.
    
    # related_name = Essa opção define um nome para o relacionamento
    # reverso. Quando você tem uma instância de uma conta, como você
    # acessa as contas que ela está seguindo? É ai que entra o related_
    # name.
    
    # MeSeguindo: Ao definir esse related_name, o Djnago cria um
    # atributo chamado MeSeguindo no nosso modelo conta. Através
    # desse atributo, você pode acessar todas as contas que a instância
    # atual está seguindo.
    
    # Observação: A coluna seguidores e seguindo basicamente irão virar
    # outras tabelas que irão conter as contas seguidas e as contas que
    # estão seguindo os usuários
    seguidores = models.ManyToManyField('self', symmetrical=False, related_name='MeSeguindo')
    
    # Ira conter todas as contas que seguimos. Segue a mesma lógica
    # da coluna de seguidores
    seguindo = models.ManyToManyField('self', symmetrical=False, related_name='ContasSeguidas')
    
    # Ira conter a foto de perfil do criador da conta. O campo ImageField
    # deve conter o caminho que o servidor irá salvar as fotos enviadas
    # pelo usuário
    foto_perfil = models.ImageField(upload_to = 'redesocial/fotos')
    
    # Irá inserir automaticamente a data de criação da conta.
    data_criacao = models.DateField(auto_now_add = True)
    
    # Ira conter o numero total de seguidores
    numero_seguidores = models.IntegerField(default=0)
    
    # Irá conter o numero total de contas seguidas pelo usuário.
    numero_seguindo = models.IntegerField(default=0)
    
    # Agora vamos criar os métodos da classe que irão administrar
    # a relação entre as contas
    
    # self: Em python orientado a objetos, quando criamos um método
    # para a nossa classe, devemos utilizar como parametro o self
    # para acessar os atributos definidos na classe. Basicamente
    # o self serve para fazer referncia aos atributos.
    
    # Método que irá adicionar seguidores na conta do usuário.
    # A função irá receber os parametros self (referencia aos 
    # atributos) e a conta que irá seguir o usuário.
    def adicionar_seguidor(self, conta_seguidor):
        
        # Iremos adicionar a nova conta na tabela de
        # seguidores
        self.seguidores.add(conta_seguidor)
        
        # Iremos adicionar a quantidade de registros da tabela 
        # seguidores na coluna de numeros de seguidores. Vamos
        # fazer essa inserção de valores usando o método count
        self.numero_seguidores = self.seguidores.count()
        
        # Ira salvar a inserção dos dados na coluna de numeros de
        # seguidores e na tabela de seguidores
        self.save()
    
    # Função que ira remover seguidores da conta do usuário: A função
    # irá receber 2 argumentos o self (referência aos atributos) e
    # a conta que será removida.
    def remover_seguidor(self, conta_seguidor_removida):
        
        # Iremos remover a conta da tabela de seguidores   
        self.seguidores.remove(conta_seguidor_removida)
        
        # Após a remoção, iremos atribuir a coluna de numeros
        # de seguidores a contagem dos registros da tabela de
        # seguidores
        self.numero_seguidores = self.seguidores.count()
        
        # Após esses comandos, vamos salvar essas alterações.
        self.save()
    
    # Função que irá permitir que o usuário siga as contas:
    # A função irá receber os argumentos self(referência aos
    # atributos) e a conta que o usuário irá seguir.
    def seguir_conta(self, conta_seguida):
        
        # Vamos adicionar a tabela de contas seguidas
        # a nova conta que o usuário irá seguir.
        self.seguindo.add(conta_seguida)
        
        # Vamos adicionar a coluna de contas seguidas
        # a quantidade de registros da tabela de contas
        # seguidas.
        self.numero_seguindo = self.seguindo.count()
        
        # Após esses comandos, vamos salvar e aplicar as alterações.
        self.save()
    
    # Função que irá permitir que o usuário deixe de seguir uma conta:
    # A função irá receber 2 argumentos self(referência aos atributos)
    # e a conta que não será mais seguida.
    def deixar_de_seguir(self, conta_nao_seguida):
        
        # Iremos remover a conta da tabela de contas seguidas
        self.seguindo.remove(conta_nao_seguida)
        
        # Ira atribuir a coluna de numeros de contas seguidas,
        # a quantidade de registros da tabela de contas seguidas
        self.numero_seguindo = self.seguindo.count()
        
        # Após esses comandos, iremos salvar essas alterações
        self.save()
    
    
    
    
    
    
    
