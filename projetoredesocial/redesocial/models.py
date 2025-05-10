
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
class Conta(models.Model):
    
    # Ira conter o nome do criador da conta
    nome = models.CharField(max_length=400)
    
    # Ira conter uma breve biografia do criador da conta
    biografia = models.CharField(max_length=1000, blank=True)
    
    # Ira conter uma breve descrição dos assuntos que 
    # criador da conta se interessa
    interesses = models.CharField(max_length=1000, blank=True)
    
    # Ira conter o estado civil do usuário
    estado_civil = models.CharField(max_length=500, blank = True)
    
    # Vamos criar uma chave estrangeira que irá relacionar o usuário 
    # a conta criada na rede, com o objetivo de atribuir um dono a
    # conta. O cascade permite que a conta relacionada ao usuário
    # também seja apagada caso o usuário seja excluido.
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
    
    # MeSeguindo: Ao definir esse related_name, o Django cria um
    # atributo chamado MeSeguindo no nosso modelo conta. Através
    # desse atributo, você pode acessar todas as contas que a instância
    # atual está seguindo.
    
    # Observação: A coluna seguidores e seguindo basicamente irão virar
    # outras tabelas que irão conter as contas seguidas e as contas que
    # estão seguindo os usuários
    seguidores = models.ManyToManyField('self', symmetrical=False, related_name='MeSeguindo')
    
    # Ira conter todas as contas que seguimos. Segue a mesma lógica
    # da coluna de seguidores.
    seguindo = models.ManyToManyField('self', symmetrical=False, related_name='ContasSeguidas')
    
    # Ira conter a foto de perfil do criador da conta. O campo ImageField
    # deve conter o caminho que o servidor irá salvar as fotos enviadas
    # pelo usuário
    foto_perfil = models.ImageField(upload_to = 'redesocial/fotos', blank=True)
    
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
        
        # Ira remover o usuário da página que ele deixou de seguir
        conta_nao_seguida.seguidores.remove(self)
        
        # Ira diminuir o numero de seguidores da página não seguida
        conta_nao_seguida.numero_seguidores = conta_nao_seguida.seguidores.count()
        
        # Iremos salvar as operações na conta que esta perdendo o
        # seguidor
        conta_nao_seguida.save()
        # Após esses comandos, iremos salvar essas alterações
        self.save()
    
    

# Essa classe ira conter todos os posts que o usuário pode fazer em
# sua conta. Por padrão as classes do models devem herdar os atributos
# de Model
class Post(models.Model):
    
    # Ira associar uma postagem ao uma conta, com o objetivo de atribuir
    # donos as postagens da rede. O método CASCADE irá possibilitarm que
    # todas as postagens seja excluidas caso o dono da postagem (conta)
    # seja removida ou excluida do sistema.
    dono_postagem = models.ForeignKey(Conta, on_delete=models.CASCADE)
    
    # Irá conter os textos das postagens. Essa coluna poderá ter valores
    # brancos que no banco de dados serão representados como nulo.
    texto = models.CharField(max_length=6000, null = True, blank=True)
    
    # Ira permitir que o usuário poste fotos e imagens na rede social. Essa coluna poderá receber
    # valores brancos que no banco de dados serão repreentados como nulo. 
    imagem_postagem = models.ImageField(upload_to = 'redesocial/ImagemPostagem', null=True, blank=True)
    
    # Ira permitir que o usuário poste videos na rede social, essa coluna poderá ter valores
    # em branco que no banco de dados será representado como nulo. 
    video = models.FileField(upload_to='redesocial/videos', null=True, blank=True)
    
    # Coluna que irá conter a quantidade de curtidas que a postagem recebeu
    # A coluna terá como valor padrão o 0.
    curtidas = models.IntegerField(default=0)
    
    # Ira conter a quantidade de deslikes que a postagem recebeu.
    #  A coluna irá receber comp valor padrão de o 0.
    nao_curtidas = models.IntegerField(default = 0)
    
    # Coluna que irá conter a quantidade de comentários do sistema.
    # A coluna irá ter como valor padrão o 0.
    quantidade_comentarios = models.IntegerField(default= 0)
    
    # Métodos que irão administrar a interação do usuário com a postagem.
    # Observação: Vale lembrar que os metodos em python em orientação a
    # objetos devem conter o parametro self que fará referência aos atributos
    # da classe, é como o this em java orientado a objetos.
    
    # Método que irá aumentar a quantidade de curtidas
    def receberCurtida(self):
        
        # Ira atribuir mais 1 na coluna de curtidas
        self.curtidas = self.curtidas + 1
        
        # Ira salvar as alterações
        self.save()
    
    # Irá adicionar deslikes na postagem
    def receberDeslike(self):
        
        # Ira adiconar mais 1 na contagem de deslikes
        self.nao_curtidas = self.nao_curtidas + 1
        
        # Ira salvar as alterações no banco de dados
        self.save()
    
    # Ira aumentar a quantidade de comentários feitos no post
    def adicionarQuantidadeComentario(self):
        
        # Ira somar a quantidade de comentários                             
        self.quantidade_comentarios = self.quantidade_comentarios + 1

        # Ira salvar as alterações no banco de dados
        self.save()
    

# Como os comentários de uma postagem possuem alguns atributos básicos
# como o autor do comentário, a sua data de criação e o seu contéudo, 
# é necessário construir uma classe que irá conter todos esses atributos
# e sua relação com as outras classes, como por exemplo, a classe Post,
# que irá conter os comentários.
class Comentarios(models.Model):
    
    # Ira relacionar um comentário a uma postagem, ela terá o
    # método de exclusão CASCADE que irá apagar todos os comentários
    # relacionados ao post caso a postagem seja excluida da página.
    postagem = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    # Ira relacionar o comentário a uma conta com o objetivo de atribuir
    # um dono ao comentário da postagem. Essa comuna também terá um método
    # exclusão de cascata
    autor = models.ForeignKey(Conta, on_delete = models.CASCADE)
    
    # Coluna que irá conter o conteúdo do comentário
    # com o limite de 6000 caracteres.
    texto_comentario = models.CharField(max_length=6000)
    
    # Coluna que irá conter a data de criação do comentario
    data_criacao = models.DateField(auto_now_add = True)    
    

    

    
    
