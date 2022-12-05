from django import forms

from .models import Usuarios, Gerais

class DateInput(forms.DateInput):
    input_type = 'date'
    
class Form_Gerais(forms.ModelForm):

    class Meta:
        model = Gerais
        fields = '__all__'
        widgets = {
            'data_do_evento': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
            
        }  
        

class Form_Usuarios(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
         
        widgets = {
            'dia': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
            
        }       
        
