

# Nesse arquivo, iremos definir todas as rotas para as views (requisições)
# do nosso sistema

from django.urls import path

from . import views


urlpatterns = [
    
    # Observação: Os names representam apelidos que iremos
    # utilizar para acessar as rotas do sistema.
    
    # Rota para a view da página inicial do sistema
    path('', views.index, name='index'),
    
    # Rota para a view da página de cadastro de usuários
    path('criarusuario', views.criarusuario, name='criarusuario'),
    
    # Rota para a view da página de login de usuários
    path('loginusuario', views.loginusuario, name='loginusuario'),
    
    # Rota para a view de criação de contas/páginas do sistema
    path('criarconta', views.criarconta, name='criarconta'),
    
    # Rota para a view de logout de usuários
    path('logoutusuario', views.logoutusuario, name='logoutusuario'),
    
    # Rota para a view de postagens do usuário
    path('posts', views.posts, name='posts')
    
    # Rota para a view de postagens do usuário
   # path('minhaconta', views.minhaconta, name='minhaconta')
    
    
    
    
    
]
