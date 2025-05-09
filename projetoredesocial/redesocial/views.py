

# Método da classe shortcuts que irá renderizar os templates
# html com as requisições e formulários de valores



from django.shortcuts import render

# Método da classe shortcuts que tem como objetivo
# redirecionar o usuário para outra página usando
# o nome da URL.
from django.shortcuts import redirect

# Método da biblioteca django.contrib.auth que tem
# como objetivo verificar se o usuário existe no sistema,
# ou seja, se é um usuário autenticado 
from django.contrib.auth import authenticate

# Método da classe django.contrib.auth que tem como objetivo
# Criar uma sessão para cada usuário que irá conter todas as
# ações do usuário autenticado, ou seja, as açoes de um  usuário
# não irá afetar as ações dos outros usuários do sistema.
from django.contrib.auth import login

# Método da biblioteca django.contrib.auth que tem como objetivo restringir as páginas apenas para usuários autenticados
from django.contrib.auth.decorators import login_required

# Método da biblioteca django.contrib.auth que encerra a sessão
# do usuário e desloga o usuário
from django.contrib.auth import logout

# import das classes que serão utilizadas no desenvolvimento
# das views.
from .models import Post, Conta, Comentarios

# Ira importar todos os formulários que iremos utilizar na construção
# das views.
from .forms import FormCriacaoConta, FormCadastroUsuario, FormLoginUsuario, FormCriacaoPost, formCriacaoComentarios

from django.http import HttpResponseRedirect
# Create your views here.

# Criação da view que irá conter todas as postagens da rede social.
# Por padrão os metodos da view devem receber como argumento o request
# que irá representar as requisições ao servidor do sistema.
def index(request):
    
    # Ira receber a classe post ira selecionar todos os objetos
    # da classe post registrados no sistema.
    post = Post.objects.all()
    
    # Por padrão o request possibilita acessar o nome dos usuários
    # (caso você tenha criado usuários com a classe User do django).
    # Então iremos acessar o nome do usuário para imprimir uma mensagem
    # de boas vindas para usuários autenticados.
    mensagem_usuario = f"Ola, {request.user.username}"
    
    # Dicionário que irá possibilitar que a gente acesse as variáveis
    # da view no template Html.
    dicionario_post = {'post':post,'mensagem_usuario':mensagem_usuario}
    
    # Retorno da função render que irá conter a requisição ao sistema,
    # o caminho do template HTML e o dicionario com as variáveis que
    # iremos acessar no template.
    return render(request,'redesocial/index.html', dicionario_post)

# View que terá como objetivo registrar usuários no sistema. A função
# irá receber como argumento o request que representa a requisição ao
# servidor do sistema
def criarusuario(request):
    
    # Primeiro, vamos verificar se a requisição é do tipo Post
    # (inserção de dados no servidor)
    if request.method == 'POST':
        
        # Se a requisição for um POST, iremos realizar as seguintes ações:
        
        # Vamos passar os dados do POST para o formulário.
        form = FormCadastroUsuario(request.POST)
        
        # Após enviar os dados para o formulário vamos verificar se
        # os dados estão seguindo as regras definidas no forms.py
        if form.is_valid():
            
            # Se os dados estiverem corretos, vamos salva-los no
            # banco de dados.
            form.save()
            
            # Após salvar os dados, iremos direcionar o usuário para
            # a página de inicio
            return redirect('index')
        
        else:
            
            # Caso os dados sejam inválidos, iremos imprimir na tela uma mensagem de
            # aviso.
            form.add_error(None, 'Dados inválidos, por favor tente novamente')
    
    else:
        
        # Se a requisição ao servidor não for um post, 
        # iremos instanciar um formulário em branco que
        # possibilitara que o usuário envie dados para o
        # sistema.
        form = FormCadastroUsuario()
    
    # Retorno da função render com a requisição ao sistema, o caminho do template
    # html e o dicionário com as variáveis que iremos acessar no template HTML.
    return render(request, 'redesocial/criarusuario.html', {'form': form})


# View que ira possbilitar que o usuário faça login no sistema.
# A função irá receber como argumento apenas a requisição ao
# sistema.
def loginusuario(request):
    
    # Primeiro, vamos verificar se o tipo de requisição
    # ao servidor é um post
    if request.method == 'POST':
        
        # Se a requisição for um post, vamos realizar os seguintes
        # comandos:
        
        # vamos passar para o formulário, os dados enviados pelo
        # usuário.
        form = FormLoginUsuario(request.POST)
        
        # Após o envio dos dados para o form, vamos verificar se os dados
        # estão seguindo as regras definidas pelo forms.py
        if form.is_valid():
            
            # Se os dados forem válidos, vamos usar a função
            # cleaned_data para acessar os campos do formulário
            # de login.
            username = form.cleaned_data['username']
            
            senha = form.cleaned_data['senha']
            
            # Após acessar os campos do form de login, vamos usar a função authenticate
            # que irá verificar se o usuário existe no sistema. Para utilizar a função
            # precisamos passar como argumento a requisição ao servidor e os campos de 
            # nome de usuário e senha
            user = authenticate(request, username = username, password = senha)
            
            # Após passar os argumentos para a função vamos verificar se um usuário
            # foi encontrado pela função.
            if user is not None:
                
                # se um usuário for encontrado, vamos utilizar a função
                # de login para criar uma sessão para esse usuário. Para
                # usar essa função precisamos passar como argumento a requisição
                # ao sistema e o authenticate com os dados do usuário encontrado.
                login(request, user)
                
                # Após o usuário entrar no sistema iremos direcionar o usuário
                # a página inicial.
                return redirect('index')
            
            else:
                
                # Se o usuário não for encontrado, vamos mostrar na tela
                # essa mensagem.
                form.add_error(None, 'Nome ou senha incorretos')
            
            
        
        else:
            
            # Caso o sistema falhe na execução do formulário, iremos apresentar
            # esse erro.
            form.add_error(None, 'Erro na execução do formulário')
    
    else:
        
        # Se a requisição ao servidor não for um post, vamos instanciar
        # um formulário em branco que possibilite que o usuário realize
        # o seu login.
        form = FormLoginUsuario()
    
    # Retorno da função de renderização de templates com as requisições ao sistema,
    # o caminho do template HTML e o dicionário que ira permitir o acesso as variáveis
    # no template HTML.
    return render(request, 'redesocial/loginusuario.html', {'form':form})

# View que irá deslogar o usuário e encerrar a sua sessão.
# A função irá receber como argumento apenas o request
# que representa as requisições ao sistema.
def logoutusuario(request):
    
    # Função logout do django que irá
    # encerrar a sessão do usuário.
    logout(request)
    
    # Após encerrar a sessão do usuário, vamos direciona-lo
    # de volta para a página inicial
    return redirect('index')


# O login required irá garantir que apenas usuários autenticados
# acessem a página de criação de contas/páginas.
@login_required

# View que irá permitir que o usuário crie um página na rede social.
# A função irá receber como parametro apenas o request que lida com
# requisições ao servidor
def criarconta(request):
    
    # Primeiro, vamos verificar o tipo de requisição feita pelo usuário
    # ao servidor.
    if request.method == 'POST':
        
        # Se a requisição for do tipo POST, iremos realizar os seguintes
        # comandos.
        
        # Vamos atribuir ao formulário os valores passados pelos usuários
        # e o arquivo com a foto de perfil do usuário
        form = FormCriacaoConta(request.POST, request.FILES)
        
        # Após envio dos dados ao formulário, vamos verificar se os dados
        # passados seguem as regras definidas no forms.py.
        if form.is_valid():
            
            # Se os dados forem válidos, vamos iniciar o processo
            # inserção dos dados no servidor 
            
            # Como dessa vez precisamos associar um usuário a uma conta,
            # vamos "Atrasar" o processo de inserção através de um commit
            # false que irá "segurar" o envio dos dados para termos tempo
            # de associar a conta a um usuário.
            conta = form.save(commit=False)
            
            # Vamos acessar a ciluna de dono da conta e atribuir a ela
            # os dados do usuário através do request.
            conta.dono_da_conta = request.user
            
            # Após a associação, vamos salvar os dados no banco de dados.
            conta.save()
            
            # Após salvar os dados no sistema vamos redirecionar o usuário para a
            # página inicial.
            return redirect('index')
        
        else: 
            
            # Se os dados não forem válidos, iremos mostrar na tela essa mensagem e o erro encontrado no formulário
            form.add_error(None, 'Dados incorretos, por favor, tente novamente')
            
            print(form.errors)
    
    
    else:
        
        # Se a requisição for diferente de um post, iremos instanciar um formulário
        # em branco que irá possibilitar que o usuário autenticado crie uma página.
        form = FormCriacaoConta()
    
    # Retorna da renderização do template com a requisição ao sistema, o
    # caminho para o template HTML e o dicionário que ira permitir o acesso
    # das variáveis da view no template HTML
    return render(request, 'redesocial/criarconta.html', {'form':form} )


# Login que irá bloquear o acesso de usuários não autenticados
@login_required
# View que irá permitir que o usuário faça postagens no sistema
def posts(request):
    
    # Primeiro, vamos verificar se a requisição é do tipo 
    # post (inserção de dados no servidor)
    if request.method == 'POST':
        
        # Se a requisição for POST, iremos realizar os seguintes comandos:
        
        # Vamos atribuir ao formulário os dados passados pelo usuário
        # e o arquivo de video e foto inserido pelo usuário
        form = FormCriacaoPost(request.POST, request.FILES)
        
        # Após o envio dos dados ao form, vamos verificar se os dados
        # passados seguem as regras definidas no forms.py
        if form.is_valid():
            
            # Se os dados forem válidos, vamos executar os seguintes
            # comandos.
            
            # Primeiro vamos dar um commit false no save do form
            # para "pausar" o salvamento dos dados no servidor, com
            # o objteivo de realizar mais validações antes da inserção
            # dos dados.
            dono_post = form.save(commit=False)
            
            # Como precisamos associar uma conta a postagem, vamos
            # dar um get (select) na coluna de dono da conta que irá
            # conter os dados do usuário que está nesse momento logado 
            # no sistema. Para isso vamos dar um get no valor da coluna
            # dono_conta que ira buscar os valores do usuário que está
            # logado no momento (representado pelo request.user).
            conta_usuario = Conta.objects.get(dono_da_conta = request.user)
        
            # Após associar as classes, vamos atribuir ao dono da postagem
            # os valores da conta do usuário que está logado.
            dono_post.dono_postagem = conta_usuario
            
           
            
            # Após todo esse processo, vamos salvar os dados no servidor
            dono_post.save()
            
            print('arquivo recebido', request.FILES)
            # Após salvar os dados, vamos direcionar o usuário para a
            # página inicial
            return redirect('index')
            
            
        else:
            
            # Se os dados não forem válidos, vamos imprimir essa mensagem
            # na tela e informar o erro no terminal do servidor
            form.add_error(None, 'Dados inválidos, por favor, tente novamente')
            
            print(form.errors)
    
    else:
        
        # Se a requisição não for um POST, iremos instanciar um
        # formulário em branco
        form = FormCriacaoPost()
    
    # Retorno da função render com a requisição ao servidor, o caminho do template HTML e o dicionário que possibilita o acesso as variáveis da view no template HTML.
    return render(request, 'redesocial/posts.html', {'form':form})


# Função que irá permitir que apenas usuários autenticados
# acessem a página
@login_required

# View que irá mostrar apenas as postagens do usuário
# autenticado. A função irá receber como argumento apenas
# o request que irá lidar com as requisições ao sistema.
def minhaconta(request):

    # Ira conter o nome do usuário autenticado no sistema
    nome_usuario = f"{request.user.username}"
    
    # Primeiro, iremos solicitar no banco de dados a conta
    # criada pelo usuário autenticado
    conta = Conta.objects.get(dono_da_conta = request.user)
    
    # Após solicitar a conta do usuário autenticado, vamos atribuir
    # essa informações ao post com o objetivo de filtrar no banco
    # de dados as informações do usuário que fez a postagem. Dessa
    # maneira iremos associar as 2 classes (posts e usuário) 
    posts = Post.objects.filter(dono_postagem = conta) 
    
    # Após a associação entre as classes, vamos criar um dicionário
    # que possibilitara que o desenvolvedor acesse as variáveis da 
    # view no template HTML.
    dicionario_post = {'posts':posts, 'nome_usuario': nome_usuario, 'conta':conta}
    
    # Retorno da função que irá renderizar o template HTML usando
    # as requisições ao servidor, o caminho do template e o dicionário
    # de variáveis da view
    return render(request, 'redesocial/minhaconta.html', dicionario_post)
    

# View que irá permitir que o usuário curta postagens de outros usuários
def curtir(request):
    
    # Primeiro vamos verificar se a requisição
    # ao servidor é do tipo POST.
    if request.method == 'POST':
    
        # Se a requisição for um post (inserção dos dados) 
        # vamos obter o id do post curtido usando o get que receberá
        # como parametro a chave (name) que iremos criar no form com
        # o botão de curtir posts. A idéia é que o get colete o id
        # do post através do formulário que ira receber como valor
        # o posts.id (coluna de ids das postagens) 
       posts_id = request.POST.get('post_id')
       
       # Após coletar as informações das postagens, vamos pegar
       # o post que possui o id igual ao id coletado
       post = Post.objects.get(id = posts_id)
       
       # Após a coleta do post, iremos chamar o método que irá realizar
       # a curtida na página
       post.receberCurtida()
       
       # Request: Como ja vimos anteriormente, ele representa as requisições que passa infromações a sua view sempre que alguma
       # ação é solicitada ao servidor.
       # META: é um dicionário python  que contém todos os cabeçalhos 
       # HTTP disponiveis na requisição. Esses cabeçalhos fornecem
       # informações adicionais sobre a requisição e o ambiente do
       # cliente.
       # HTTP_REFERER: O get irá obter o HTTP_REFERER que é o caminho da
       # página atual do usuário.
       pagina_atual = request.META.get('HTTP_REFERER')
       
       # Esta é uma classe do Django que representa uma resposta HTTP 
       # com um código de status de redirecionamento (geralmente 302
       # found). Quando o navegador do usuário recebe essa resposta,
       # ele automaticamente faz uma nova requisição para URL especificada
       # como argumento. No nosso caso vamos passar como parametro o 
       # caminho da página atual que o usuário está no momento em que 
       # curtiu uma postagem.
       return  HttpResponseRedirect(pagina_atual)
   
   

# View que irá permitir que outros usuários não curta as
# postagens realizadas pelos usuários. A função irá receber
# como parametro apenas o request que lida com requisições
# no sistema.
def nao_curtir(request):
    
    # Antes de iniciar o processo, vamos verificar se o usuário
    # fez uma requisição POST ao servidor.
    if request.method == 'POST':
        
        # Se a requisição for do tipo POST, Iremos realizar os seguintes
        # comandos:
        
        # Vamos atribuir a variável o valor do id presente
        # no form que contém o name 'nao_curtir_post'
        id_post = request.POST.get('nao_curtir_post')
        
        # Após atribuir o valor na variável, vamos buscar no
        # banco de dados o post que contém o id presente no 
        # form.
        post = Post.objects.get(id=id_post)
        
        # Após selecionar o id da postagem, vamos chamar o método
        # de receberDeslike que irá incrementar a contagem de 
        # 'não curtidas' da postagem que contém o id especificado.
        post.receberDeslike()
        
        # Serve para pegar o endereço da página que o usuário
        # está no momento da interação com a página.
        pagina_atual = request.META.get('HTTP_REFERER')
        
        # Após realizar todos os comandos, vamos retornar um httpresponse
        # redirect que irá enviar a requisição do método de deslike e
        # direcionará o usuário para a página que ele estava anterior
        # mente.
        return HttpResponseRedirect(pagina_atual)


# Função que irá garantir que apenas usuários autenticados
# acessem a página
@login_required

# View que irá permitir que outros usuários comentem as postagens.
# A função ira receber como parametro o requst que lida com requisições
# e o id da postagem que será comentada
def comentar_publicacao(request, post_id):
    
    # Primeiro, vamos acessar a postagem comentada
    # via id
    post = Post.objects.get(id=post_id)
    
    # Após acessar o post comentado via id, vamos verificar
    # se a requisição ao servidor é do tipo POST.
    if request.method == 'POST':
        
        # Se a requisição for um POST, vamos realizar os seguintes comandos
        
        # Primeiro, vamos passar para o formulário, os dados
        # inseridos pelo usuário
        form = formCriacaoComentarios(request.POST)
        
        # Após passar os dados para o formulário, vamos
        # verificar se os dados seguem as regras definidas
        # no forms.py
        if form.is_valid():
            
            # Primeiro, vamos atrasar o salvamento dos dados no servidor
            # com o objetivo de fazer algumas validações antes de salvar
            # os dados no banco de dados.
            comentarios = form.save(commit=False)
            
            # Após atrasar o salvamento vamos iniciar o processo de associação
            # entre as classes.
            
            # Atribuindo a coluna autor o dono da conta que esta fazendo o comentário.
            # Para isso, vamos acessar a conta que possui a coluna dono_da_conta igual
            # ao usuário autenticado (usuário que está realizando o comentário na postagem)
            comentarios.autor = Conta.objects.get(dono_da_conta = request.user)
            
            # Como ja acessamos anteriormente a postagem que contém o id da
            # postagem comentada, vamos atribuir a coluna de postagem, o post
            # que está sendo comentado no momento. 
            comentarios.postagem = post
            
            # Após realizar todas as associações, vamos salvar os dados
            # no servidor
            comentarios.save()
            
            # Após salvar os dados vamos incrementar a contagem de comentários da postagem
            post.adicionarQuantidadeComentario()
            
            # Por último iremos direcionar novamente o usuário para a página inicial.
            return redirect('index')
    
    
        else:
            
            # Se algo der errado na inserção de comentários, iremos apresentar essa
            # mensagem.
            form.add_error(None, 'Dados inválidos, por favor tente novamente')
    
    else:
        
        # Se a requisição não for um POST, iremos instanciar um formulário
        # em branco que possibilitara que o usuário insira um novo comentário.
        form = formCriacaoComentarios()

    # Retorno da função que irá renderizar o template html. A função ira receber a requisição
    # ao servidor, o caminho do template html, e o dicionário que irá possibilitar o acesso
    # das variáveis da view no template
    return render(request, 'redesocial/comentar_publicacao.html', {'form':form, 'post':post})



# View que irá apresentar os comentarios de cada post
# registrado no sistema. A função irá receber como
# parametro o request que lida com requisições e o id
# do post que contém os comentários.
def ver_comentarios(request, post_id):
    
    # Priemiro, vamos acessar a postagem que contém o id acessado
    post = Post.objects.get(id=post_id)
    
    # Agora vamos acessar apenas os comentarios da postagem que
    # contém o id acessado no sistema.
    comentarios = Comentarios.objects.filter(postagem=post)
    
    # Após acessar a psotagem e seus comentários, iremos 
    # criar um dicionário que irá permitir acessar as variáveis
    # no template HTML.
    dicionario_post = {'post':post, 'comentarios':comentarios}
    
    # Retorna da função que irá renderizar o template HTML. A
    # função irá receber como parametro o request com as requisições
    # ao servidor.
    return render(request, 'redesocial/ver_comentarios.html', dicionario_post)
            


# Irá proteger a página de usuários não autenticados
@login_required
# View que irá possibilitar que uma conta siga a outra 
# na rede social. A função irá receber apenas o request 
# que lida com requisições
def seguir(request):
        
        # Primeiro vamos acessar o id presente no form 
        # do index que irá conter o id da conta que realizou
        # uma determinada postagem na rede social. O acesso
        # ao id será feito via o name do form que irá transferir
        # para a variável o valor presente no value do forms (no
        # caso o id da conta que realizou a postagem)
        id_conta = request.POST.get('id_conta')
        
        # Após acessar o id, vamos utiliza-lo para acessar a conta
        # que será seguida pelo usuário
        conta_seguida = Conta.objects.get(id=id_conta)
        
        # Agora vamos acessar a conta do usuário autenticado
        # para realizarmos o processo de seguir a conta desejada.
        conta_que_ira_seguir = Conta.objects.get(dono_da_conta=request.user)
        
        # Agora que ja acessamos as 2 contas, vamos chamar os metodos
        # adicionar seguidores e de seguir contas
        
        # Ira representar o usuário autenticado que irá seguir a conta.
        # A função irá receber como parametro a conta que o usuário
        # irá seguir.
        conta_que_ira_seguir.seguir_conta(conta_seguida)
        
        # Ira representar a conta seguida. A função irá receber
        # como parametro a conta que esta seguindo a conta que
        # realizou a postagem
        conta_seguida.adicionar_seguidor(conta_que_ira_seguir)
        
         # Serve para pegar o endereço da página que o usuário
        # está no momento da interação com a página.
        pagina_atual = request.META.get('HTTP_REFERER')
        
        # Ira enviar as requisições ao servidor e direcionará
        # o usuário para a página que ele estava antes de realizar
        # a ação de seguir contas.
        return HttpResponseRedirect(pagina_atual)    



@login_required
def meus_seguidores(request):
    
    conta = Conta.objects.get(dono_da_conta = request.user)
    
    mensagem_seguidores = f'Seguidores da página do (a) {request.user.username}'
    
    numero_seguidores = conta.numero_seguidores
    
    seguidores = conta.seguidores.all()
    
    
    dicionario_seguidores = {'mensagem_seguidores':mensagem_seguidores, 'seguidores':seguidores, 'numero_seguidores':numero_seguidores}
    
    return render(request, 'redesocial/meus_seguidores.html', dicionario_seguidores)