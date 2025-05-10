

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
    path('posts', views.posts, name='posts'),
    
    # Rota para a view de postagens do usuário
    path('minhaconta', views.minhaconta, name='minhaconta'),
    
    # Rota para a view de curtir postagens.
    path('curtir', views.curtir, name='curtir'),
    
    # Rota para view de não curtir postagens
    path('nao_curtir', views.nao_curtir, name='nao_curtir'),
    
    # Rota para view de comentar publicação. Nesse caso será necessário
    # especificar o id da postagem que estára recebendo o comentário.
    path('comentar_publicacao/<int:post_id>/', views.comentar_publicacao, name='comentar_publicacao'),
    
    
    # Rota para a view que ira mostrar todos os comentários da postagem.
    # Ela irá receber como parametro o id da postagem que irá conter os
    # comentários
    path('ver_comentarios/<int:post_id>/', views.ver_comentarios, name='ver_comentarios'),
    
    # Rota para view que irá permitir que uma conta siga a outra
    # na rede social.
    path('seguir', views.seguir, name='seguir'),
    
    # Rota para view que irá mostrar todos os seguidores de uma conta
    
    path('meus_seguidores', views.meus_seguidores, name='meus_seguidores'),
    
    # Rota para a view que mostra todas as contas que o usuário
    # segue na rede social
    path('quem_sigo', views.quem_sigo, name='quem_sigo'),
    
    path('deixar_de_seguir', views.deixar_de_seguir, name='deixar_de_seguir'),
    
    
] 
