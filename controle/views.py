from django.shortcuts import render
from urllib.request import Request
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .forms import Form_Usuarios, Form_Gerais
from django.contrib.auth.decorators import login_required
from .models import Usuarios, Gerais
from django.contrib import messages

def gerais(request):
    gerais = Gerais.objects.all()
    return render(request, 'templates/gerais.html', {'gerais': gerais}) 

def add_gerais(request):
    
    if request.method == 'POST':
        gerais = Form_Gerais(request.POST)
        
        if gerais.is_valid() :
            gerais.save()
            gerais = Form_Gerais()

            messages.info(request, 'Inserido com sucesso')
            return redirect('/gerais')
 
    else:
        gerais = Form_Gerais()
    
    return render(request, 'templates/add_gerais.html', {'gerais': gerais})   

def editar_gerais(request, id):
    editar_gerais = get_object_or_404(Gerais, pk=id)
    form = Form_Gerais(instance=editar_gerais)
 
    if request.method == 'POST':
        form = Form_Gerais(request.POST, instance=editar_gerais)
         
        if form.is_valid():
            editar_gerais.save()
            messages.info(request, 'Editado com sucesso')
            return redirect('/gerais')
   
        else:
            return render(request, 'templates/editar_gerais.html', {'form':form ,'editar_gerais': editar_gerais})  

    return render(request, 'templates/editar_gerais.html', {'form':form ,'editar_gerais': editar_gerais})  
    
def deletar_gerais(request):
    del_gerais = Gerais.objects.all()
   
    if request.method == 'POST':
        del_gerais.delete()

        messages.info(request, 'Apagado com sucesso')
        return redirect('/gerais')

    return render(request, 'templates/deletar_gerais.html')  
    

def home(request):
    return render(request, 'templates/home.html') 

def add_usuario(request):
    if request.method == 'POST':
        usuario = Form_Usuarios(request.POST)
        
    
        if usuario.is_valid():
            usuario.save()
          
            usuario = Form_Usuarios()
 
            messages.info(request, 'Inserido com sucesso')
            return redirect('/add_usuario')
       
    else:
        usuario = Form_Usuarios()
    
    return render(request, 'templates/add_usuario.html', {'usuario': usuario,})   

def lista_usuario(request):
    lista = Usuarios.objects.all()
    quantidade = Usuarios.objects.all().count()
    return render(request, 'templates/lista_usuario.html', {'lista': lista, 'quantidade': quantidade})
   
def editar_lista(request, id):
    editar = get_object_or_404(Usuarios, pk=id)
    form = Form_Usuarios(instance=editar)
 
    if request.method == 'POST':
        form = Form_Usuarios(request.POST, instance=editar)
         
        if form.is_valid():
            editar.save()
            messages.info(request, 'Editado com sucesso')
            return redirect('/lista_usuario')
   
        else:
            return render(request, 'templates/editar_lista.html', {'form':form ,'editar': editar})  


    return render(request, 'templates/editar_lista.html', {'form':form ,'editar': editar})  

def deletar_usuario(request, id):
    deletar = get_object_or_404(Usuarios, pk=id)
   
    if request.method == 'POST':
        deletar.delete()

        messages.info(request, 'Apagado com sucesso')
        return redirect('/lista_usuario')

    return render(request, 'templates/deletar_usuario.html')         

def organizar(request):
    organizar = Usuarios.objects.order_by('poltrona').all()
    return render(request, 'templates/organizar.html', {'organizar': organizar, })   

def editar_poltrona(request,id):
    editar = get_object_or_404(Usuarios, pk=id)
    form = Form_Usuarios(instance=editar)
 
    if request.method == 'POST':
        form = Form_Usuarios(request.POST, instance=editar)
         
        if form.is_valid():
            editar.save()
            messages.info(request, 'Editado com sucesso')
            return redirect('/organizar')
   
        else:   

            return render(request, 'templates/editar_poltrona.html',{'form':form ,'editar_gerais': editar})   
    
    return render(request, 'templates/editar_poltrona.html', {'form':form ,'editar_gerais': editar})   