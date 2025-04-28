

# 
from django import forms

from django.contrib.auth.forms import UserCreationForm

from.models import Conta

from. models import Post

from .models import Comentarios


class FormCadastroUsuario(UserCreationForm):
        
        pass


class FormLoginUsuario(forms.Form):
        
        
        username = forms.CharField(max_length=400, label="Nome de usuário", required=True)
        
        
        senha = forms.CharField(max_length=8, label='Senha', required=True)



class FormCriacaoConta(forms.ModelForm):
        
        class Meta:
                
                model = Conta
                
                fields = ['nome', 'biografia', 'interesses', 'estado_civil', 'foto_perfil' ]
                
                labels = {
                        
                         'nome:':'Nome da conta',
                        
                         'biografia':'Biografia',
                        
                         'interesses': 'Interesses',
                         
                         'estado_civil': 'Estado Civil',
                         
                         'foto_perfil': 'Foto de Perfil'
                }
                
                
                widgets = {
                        
                        'interesses': forms.Textarea(attrs={'rows': 5, 'cols':40}),
                        
                        'biografia': forms.Textarea(attrs={'rows': 5, 'cols':40})
                }
                

    
    
    
    



    
    
    
    
        