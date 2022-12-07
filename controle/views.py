from django.shortcuts import render
from urllib.request import Request
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .forms import Form_Usuarios, Form_Gerais
from django.contrib.auth.decorators import login_required
from .models import Usuarios, Gerais
from django.contrib import messages
from fillpdf import fillpdfs
import pywhatkit
from pdf2image import convert_from_path
import win32clipboard
import glob, sys, fitz

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
  
def recibo(request, id):
    gerais = get_object_or_404(Gerais)
    usuarios = get_object_or_404(Usuarios, pk=id) 
    formgerais = Form_Gerais(instance=gerais)
    formusuarios = Form_Usuarios(instance=usuarios)
    
    
    congregacao = formgerais['congregação'].value()
    valor_da_passagem = formgerais['valor_da_passagem'].value()
    nome = formusuarios['nome'].value()
    evento = formgerais['evento'].value() 
    data_do_evento1 = formgerais['data_do_evento'].value()
    data_do_evento = data_do_evento1.strftime("%d-%m-%Y")
    cidade = formgerais['cidade'].value()    
    dia = formusuarios['dia'].value().strftime("%d-%m-%Y")
    coordenador = formgerais['coordenador'].value()
    assistente = formgerais['assistente'].value()
    telefone = formusuarios['telefone'].value()
    
    

 
    data_dict = {
                "congregacao":congregacao,
                "valor_da_passagem": valor_da_passagem,
                "nome": nome,
                "evento": evento,
                'data_do_evento':data_do_evento,
                'cidade': cidade,
                'dia': dia,
                'coordenador':coordenador,
                'assistente': assistente,
                
            }
                
    fillpdfs.write_fillable_pdf('static/recibo.pdf', 'static/recibo_pronto.pdf', data_dict)
    
    pages = convert_from_path('static/recibo_pronto.pdf', 500)
    for page in pages:
        page.save('static/recibo.png', 'PNG')
    
            
    if request.method == 'POST':
        pywhatkit.sendwhats_image("+55" + telefone, "static/recibo.png")
        
    
    return render(request, 'templates/recibo.html', {'formgerais':formgerais ,'formusuarios': formusuarios, 'gerais': gerais, 'usuarios': usuarios, 'telefone': telefone})  
   
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