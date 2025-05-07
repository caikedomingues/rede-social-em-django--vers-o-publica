

# Nesse arquivo iremos definir todos os formulários
# necessários para o desenvolvimento do sistema
from django import forms

# Import da classe UseCreationForm que irá criar
# formulários de criação de User no sistema
from django.contrib.auth.forms import UserCreationForm

# Import das classes models que iremos utilizar na construção dos
# forms
from.models import Conta

from. models import Post

from .models import Comentarios


# Criação do formulário de criação de novos usuários.
# Essa classe ira herdar os atributos da classe 
# UseCreationForm que tem como objetivo criar 
# usuários User (da classe User) no sistema.
class FormCadastroUsuario(UserCreationForm):

        # Como não vamos personalizar as informações de cadastro
        # vamos passar o atributo pass que simboliza que a classe
        # não terá nada além dos atributos herdados
        pass


# Criação do formulário de de login de usuários. A função ira herdar 
# os métodos e da classe forms que irá possibilitar a criação dos
# campos do formulário de login.
class FormLoginUsuario(forms.Form):
        
        # Campo que irá conter o nome de usuário de até 400 caracteres.
        # Esse campo ira conter um rótulo e um required true que irá 
        # sinalizar que o campo é obrigatório.
        username = forms.CharField(max_length=400, label="Nome de usuário", required=True)
        
        # Campo que irá conter a senha do usuário de até 8  caracteres.
        # Esse campo ira conter um rótulo e um required true que irá 
        # sinalizar que o campo é obrigatório.
        senha = forms.CharField(max_length=8, label='Senha', required=True)



# Criação do formulário de criação de páginas da rede social. Essa classe
# ira herdar os atributos da classe ModelForm que tem como objetivo adquirir
# as caracteristicas dos models definidos no nosso banco de dados, dessa maneira,
# não precisamos passar as propriedades do campo, já que o modelform ja ira 
# extrair essas caracterristicas das nossas classes.
class FormCriacaoConta(forms.ModelForm):
        
        # Classe que irá configurar o modelForm 
        class Meta:
                
                # Classe que iremos utilizar na construção do forms
                model = Conta
                
                # Campos do formulário que são representados pelos atributos definidos na classe
                # Conta
                fields = ['nome', 'biografia', 'interesses', 'estado_civil', 'foto_perfil' ]
                
                # Dicionário de rótulos dos campos do form, onde associamos um rótulo a um
                # campo
                labels = {
                        
                         'nome:':'Nome da conta',
                        
                         'biografia':'Biografia',
                        
                         'interesses': 'Interesses',
                         
                         'estado_civil': 'Estado Civil',
                         
                         'foto_perfil': 'Foto de Perfil'
                }
                
                
                # Widget que irá criar um text area para os campos de biografia
                # e interesses
                widgets = {
                        
                        'interesses': forms.Textarea(attrs={'rows': 5, 'cols':40}),
                        
                        'biografia': forms.Textarea(attrs={'rows': 5, 'cols':40})
                }
                

    
    
# Formulário de criação de psotagens. A classe ira herdar o model forms
# que irá extrair as caracteridticas definidas no models, ou seja, não
# precisamos personalizar o form, pois, ele ja ira conter as propreidades
# de cada atributo da classe utilizada.    
class FormCriacaoPost(forms.ModelForm):
        
        # Classe de configuração da classe 
        class Meta:
                
                # Classe que vamos utilizar na construção do form.
                model = Post
                
                # Atributos da classe Post que se tornarão campos no
                # formulário.
                fields = ['texto', 'imagem_postagem', 'video']
                
                # Dicionário de rótulos dos campos do formulario,
                # onde iremos associar os campos aos rótulos.
                labels = {
                        
                        'texto':'Escreva o que você está pensando',
                        
                        'imagem_postagem': 'Publique uma foto',
                        
                        'video': 'Publique um video'
                }    


# Criação do formulário de inserção de comentários. Como queremos que
# o campo tenha as mesmas propriedades do atributo definido no model
# (classe de criação de tabelas para o banco de dados), vamos fazer
# a classe herdar o ModelForm do módulo forms
class formCriacaoComentarios(forms.ModelForm):
        
        # Classe que irá permitir a configuração dos atributos
        # ModelForm.
        class Meta:
                
                # O model irá receber a classe que iremos utilizar
                # na construção do formulário
                model = Comentarios
                
                # Ira conter um campo que será o atributo texto_comentario
                # definido na classe Comentarios do arquivo models
                fields = ['texto_comentario']
                
                # Dicionário que irá conter o rótulo do formulário
                # criado
                labels = {
                        
                        'texto_comentario': 'Escreva o que voce acha sobre essa postagens'
                }
                
                # Ira transformar o campo do formulário em um textarea
                # de 5 linahs e 40 linhas.
                widgets = {
                        
                        'texto_comentario': forms.Textarea(attrs={'rows': 5, 'cols':40}),
                }

    
    
    
    
        