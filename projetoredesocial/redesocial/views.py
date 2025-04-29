

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

# Ira import das classes utilizadas na criação dos posts 
from .models import Post, Conta

# Ira importar todos os formulários que iremos utilizar na construção
# das views.
from .forms import FormCriacaoConta, FormCadastroUsuario, FormLoginUsuario, FormCriacaoPost
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
        form = FormCriacaoConta(request.POST)
        
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
        form = FormCriacaoPost(request.POST)
        
        # Após o envio dos dados ao form, vamos verificar se os dados
        # passados seguem as regras definidas no forms.py
        if form.is_valid():
            
            # Se os dados forem válidos, vamos iniciar o processo
            # de salvar os dados no servidor.
            
            # Primeiro, vamos "atrasar" o salvamento dos dados
            # usando o commit false, dessa maneira, conseguiremos
            # fazer a associação da postagem com a conta do usuario.
            dono_post = form.save(commit=False)
            
            conta = Conta()
            # Após o commit false vamos atribuir a coluna de 
            # de dono de postagens, os dados do usuário que está
            # autenticado no sistema. A atribuição ocorre através do método request.
            dono_post.dono_postagem = conta.nome
            # Após a associação entre as classes, iremos salvar os dados no banco de dados
            dono_post.save()
            
        
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