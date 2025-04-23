

# Nesse arquivo, iremos definir todas as rotas para as views (requisições)
# do nosso sistema

from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    
    
]
