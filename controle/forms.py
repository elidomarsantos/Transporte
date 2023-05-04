from django import forms

from .models import Usuarios, Gerais_Assembleia, Usuarios_Assembleia, Gerais_Congresso_Sexta, Usuarios_Congresso_Sexta, Gerais_Congresso_Sabado, Usuarios_Congresso_Sabado, Gerais_Congresso_Domingo, Usuarios_Congresso_Domingo

class DateInput(forms.DateInput):
    input_type = 'date'
    
class Form_Gerais_Assembleia(forms.ModelForm):

    class Meta:
        model = Gerais_Assembleia
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
        
class Form_Usuarios_Assembleia(forms.ModelForm):
    class Meta:
        model = Usuarios_Assembleia
        fields = '__all__'
         
        widgets = {
            'dia': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
            
        }   
class Form_Gerais_Congresso_Sexta(forms.ModelForm):

    class Meta:
        model = Gerais_Congresso_Sexta
        fields = '__all__'
        widgets = {
            'data_do_evento': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
            
        }  
        
class Form_Usuarios_Congresso_Sexta(forms.ModelForm):
    class Meta:
        model = Usuarios_Congresso_Sexta
        fields = '__all__'
         
        widgets = {
            'dia': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
            
        }           
        
class Form_Gerais_Congresso_Sabado(forms.ModelForm):

    class Meta:
        model = Gerais_Congresso_Sabado
        fields = '__all__'
        widgets = {
            'data_do_evento': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
            
        }  
        
class Form_Usuarios_Congresso_Sabado(forms.ModelForm):
    class Meta:
        model = Usuarios_Congresso_Sabado
        fields = '__all__'
         
        widgets = {
            'dia': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
            
        }  
        
class Form_Gerais_Congresso_Domingo(forms.ModelForm):

    class Meta:
        model = Gerais_Congresso_Domingo
        fields = '__all__'
        widgets = {
            'data_do_evento': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
            
        }  
        
class Form_Usuarios_Congresso_Domingo(forms.ModelForm):
    class Meta:
        model = Usuarios_Congresso_Domingo
        fields = '__all__'
         
        widgets = {
            'dia': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
            
        }                                            