"""
URL configuration for projetoredesocial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Nesse arquivo iremos incluir as urls do app que iremos criar para o projeto. Ao incluir aqui as urls do app, 

# Importa o módulo para a interface administrativa do Django.
# O django fornece uma interface de administração poderosa 
# pronta para uso para gerenciar os dados do seu aplicativo.
from django.contrib import admin

# Importa a função path que é usada para definir um padrão URL
# e associa-lo a uma view (função que processa a requisição e
# retorna a resposta).
from django.urls import path

# Importa a função include, que permite incluir URLS de outros
# arquivos de configuração (geralmente dos aplicativos djangos).
# Isso ajuda a manter o arquivo urls.py principal organizado.
from django.urls import include

# Importa a função static, que é usada para servir arquivos estatisticos
# (como imagens, CSS, javascipt) durante o desenvolvimento. Em produção, 
# geralmente um servidor web dedicado(como Nginx ou Apache) serve esses
# arquivos de forma eficiente.
from django.conf.urls.static import static

# Importa o módulo settings da biblioteca conf, que contém todas as
# configurações do seu projeto Django (Incluindo configurações para
# arquivos estatisticos e media)
from django.conf import settings


# Lista das urls do sistema
urlpatterns = [
    # Rota para administradores do sistema
    path('admin/', admin.site.urls),
    
    # Rota para o sistema: Se a url estiver vázia após a barra do endereço do sistema, vamos direcionar o usuário para o nosso site.
    path('', include('redesocial.urls')),

    # Adiciona o resultado da função static a lista de urls do sistema.
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT): Esta
    # função é usada para configurar como o Django serve os arquivos de
    # midia (arquivos enviados pelos usuários como imagens de perfil, fotos de posts, etc) durante o desenvolvimento.
    
    # document_root=settings.MEDIA_ROOT: É outra configuração np settings.py que especifica o caminho do diretório no seu sistema de arquivos
    # onde os arquivos de midia são armazenados.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
