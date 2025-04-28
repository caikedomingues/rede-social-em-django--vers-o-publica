

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

# Ira importar a classe Post do models 
from .models import Post

# Ira importar todos os formulários que iremos utilizar na construção
# das views.
from .forms import FormCriacaoConta, FormCadastroUsuario, FormLoginUsuario
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
            
            
            form.save()
            
            return redirect('index')
        
        else:
            
            form.add_error(None, 'Dados inválidos, por favor tente novamente')
    
    else:
        
        form = FormCadastroUsuario()
    
    
    return render(request, 'redesocial/criarusuario.html', {'form': form})



def loginusuario(request):
    
    if request.method == 'POST':
        
        form = FormLoginUsuario(request.POST)
        
        if form.is_valid():
            
            
            username = form.cleaned_data['username']
            
            senha = form.cleaned_data['senha']
            
            user = authenticate(request, username = username, password = senha)
            
            if user is not None:
                
                login(request, user)
                
                return redirect('index')
            
            else:
                
                form.add_error(None, 'Nome ou senha incorretos')
            
            
        
        else:
            
            form.add_error(None, 'Erro na execução do formulário')
    
    else:
        
        form = FormLoginUsuario()
    
    
    return render(request, 'redesocial/loginusuario.html', {'form':form})


def logoutusuario(request):
    
    logout(request)
    
    return redirect('index')



@login_required
def criarconta(request):
    
    if request.method == 'POST':
        
        form = FormCriacaoConta(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('index')
        
        else: 
            
            form.add_error(None, 'Dados incorretos, por favor, tente novamente')
    
    
    else:
        
        form = FormCriacaoConta()
    
    
    return render(request, 'redesocial/criarconta.html', {'form':form} )