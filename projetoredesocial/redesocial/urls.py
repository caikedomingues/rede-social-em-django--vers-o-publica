

# Nesse arquivo, iremos definir todas as rotas para as views (requisições)
# do nosso sistema

from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    
    path('criarusuario', views.criarusuario, name='criarusuario'),
    
    path('loginusuario', views.loginusuario, name='loginusuario'),
    
    path('criarconta', views.criarconta, name='criarconta'),
    
    path('logoutusuario', views.logoutusuario, name='logoutusuario')
    
    
    
]
