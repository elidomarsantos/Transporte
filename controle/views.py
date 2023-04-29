from django.shortcuts import render
from urllib.request import Request
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .forms import Form_Usuarios, Form_Gerais_Assembleia, Form_Usuarios_Assembleia
from django.contrib.auth.decorators import login_required
from .models import Usuarios, Gerais_Assembleia, Usuarios_Assembleia
from django.contrib import messages
from fillpdf import fillpdfs
import pandas as pd
import os
from django.http import FileResponse, HttpResponseBadRequest

def home(request):
    return render(request, 'templates/home.html') 

def inicial(request):
    return render(request, 'templates/inicial.html') 

def add_usuario(request):
    if request.method == 'POST':
        usuario = Form_Usuarios(request.POST)
   
        if usuario.is_valid():
            gerais = usuario.save(commit=False)
            assembleia = Usuarios_Assembleia(
                nome=usuario.cleaned_data['nome'],
                identidade=usuario.cleaned_data['identidade'],
                telefone=usuario.cleaned_data['telefone'],
                observações=usuario.cleaned_data['observações']
                )
            
            gerais.save()
            assembleia.save()
          
            usuario = Form_Usuarios()
 
            messages.info(request, 'Inserido com sucesso')
            return redirect('/add_usuario')
       
    else:
        usuario = Form_Usuarios()
    
    return render(request, 'templates/add_usuario.html', {'usuario': usuario,})   
def lista_usuario(request):
    lista = Usuarios.objects.order_by('nome').all()
    quantidade = Usuarios.objects.all().count()
    
   
    return render(request, 'templates/lista_usuario.html', {'lista': lista, 'quantidade': quantidade})

def editar_lista(request, id):
    editar = get_object_or_404(Usuarios, pk=id)
    form = Form_Usuarios(instance=editar)
 
    if request.method == 'POST':
        form = Form_Usuarios(request.POST, instance=editar)
         
        if form.is_valid():
            editar.save()
           
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

def assembleia(request):
    gerais = Gerais_Assembleia.objects.all()
    return render(request, 'templates/assembleia.html', {'gerais': gerais}) 

def add_gerais_assembleia(request):
    
    if request.method == 'POST':
        gerais = Form_Gerais_Assembleia(request.POST)
        
        if gerais.is_valid() :
            gerais.save()
            gerais = Form_Gerais_Assembleia()

            messages.info(request, 'Inserido com sucesso')
            return redirect('/assembleia')
 
    else:
        gerais = Form_Gerais_Assembleia()
    
    return render(request, 'templates/add_gerais_assembleia.html', {'gerais': gerais})   

def editar_gerais_assembleia(request, id):
    editar_gerais = get_object_or_404(Gerais_Assembleia, pk=id)
    form = Form_Gerais_Assembleia(instance=editar_gerais)
 
    if request.method == 'POST':
        form = Form_Gerais_Assembleia(request.POST, instance=editar_gerais)
         
        if form.is_valid():
            editar_gerais.save()
            
            return redirect('/assembleia')
 
   
        else:
            return render(request, 'templates/editar_gerais_assembleia.html', {'form':form ,'editar_gerais': editar_gerais})  

    return render(request, 'templates/editar_gerais_assembleia.html', {'form':form ,'editar_gerais': editar_gerais})  
    
def deletar_gerais_assembleia(request):
    del_gerais = Gerais_Assembleia.objects.all()
   
    if request.method == 'POST':
        del_gerais.delete()

        return redirect('/assembleia')

    return render(request, 'templates/deletar_gerais_assembleia.html')  
 
def organizar_assembleia(request):
    
    imprimir = Usuarios_Assembleia.objects.all().values()
    quantidade = Usuarios_Assembleia.objects.all()
    organizar = Usuarios_Assembleia.objects.all()
    
    df = pd.DataFrame(imprimir)
    df.to_excel("static/Usuarios.xlsx", header=True, index=False)
    print(organizar)
  
    return render(request, 'templates/organizar_assembleia.html', {'quantidade': quantidade,'organizar': organizar})   

def editar_lista_assembleia(request, id):
    editar = get_object_or_404(Usuarios_Assembleia, pk=id)
    form = Form_Usuarios_Assembleia(instance=editar)
 
    if request.method == 'POST':
        form = Form_Usuarios_Assembleia(request.POST, instance=editar)
         
        if form.is_valid():
            editar.save()
            messages.info(request, 'Editado com sucesso')
            return redirect('/organizar_assembleia')
   
        else:
            return render(request, 'templates/editar_lista_assembleia.html', {'form':form ,'editar': editar})  


    return render(request, 'templates/editar_lista_assembleia.html', {'form':form ,'editar': editar})  

def deletar_usuario_assembleia(request, id):
    deletar = get_object_or_404(Usuarios_Assembleia, pk=id)
   
    if request.method == 'POST':
        deletar.delete()

       
        return redirect('/organizar_assembleia')

    return render(request, 'templates/deletar_usuario_assembleia.html')


def poltrona_assembleia(request, id):
    gerais = get_object_or_404(Gerais_Assembleia)
    usuarios = get_object_or_404(Usuarios_Assembleia, pk=id) 
    formgerais = Form_Gerais_Assembleia(instance=gerais)
    formusuarios = Form_Usuarios_Assembleia(instance=usuarios)
    
    
    
    nome = formusuarios['nome'].value()
    data_do_evento1 = formgerais['data_do_evento'].value()
    data_do_evento = data_do_evento1.strftime("%d-%m-%Y")
    poltrona = formusuarios['poltrona'].value()
    carro = formusuarios['carro'].value()
    
 
    data_dict = {
                
                "nome": nome,
                'data_do_evento':data_do_evento,
                'poltrona': poltrona,
                'carro': carro,
                
            }
                
    fillpdfs.write_fillable_pdf('static/passagem_assembleia.pdf', 'static/passagem_assembleia_pronta.pdf', data_dict)
    
    extensão = '.pdf'
    pasta = 'static/'
    nome_antigo = 'static/passagem_assembleia_pronta.pdf'
    novo_nome = 'Passagem de' + ' ' + nome + extensão 
   

    if os.path.exists(novo_nome):
        os.remove(novo_nome)

    os.rename(nome_antigo, novo_nome)
    
    caminho_arquivo = novo_nome
      
    try:
        response = FileResponse(open(caminho_arquivo, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(novo_nome)
        return response
    except Exception:
        return HttpResponseBadRequest('Erro ao baixar o arquivo')

    return render(request, 'templates/poltrona.html', {'formgerais':formgerais ,'formusuarios': formusuarios, 'gerais': gerais, 'usuarios': usuarios, })   

def recibo_assembleia(request, id):
    gerais = get_object_or_404(Gerais_Assembleia)
    usuarios = get_object_or_404(Usuarios_Assembleia, pk=id) 
    formgerais = Form_Gerais_Assembleia(instance=gerais)
    formusuarios = Form_Usuarios_Assembleia(instance=usuarios)
    
    
    congregacao = formgerais['congregação'].value()
    valor_da_passagem = formgerais['valor_da_passagem'].value()
    nome = formusuarios['nome'].value()
    data_do_evento1 = formgerais['data_do_evento'].value()
    data_do_evento = data_do_evento1.strftime("%d-%m-%Y")
    cidade = formgerais['cidade'].value()    
    estado = formgerais['estado'].value()
    coordenador = formgerais['coordenador'].value()
    assistente = formgerais['assistente'].value()
  
    data_dict = {
                "congregacao":congregacao,
                "valor_da_passagem": valor_da_passagem,
                "nome": nome,
                'data_do_evento':data_do_evento,
                'cidade': cidade,
                'estado': estado,
                'coordenador':coordenador,
                'assistente': assistente,
                
            }
                
    fillpdfs.write_fillable_pdf('static/recibo_assembleia.pdf', 'static/recibo_assembleia_pronto.pdf', data_dict)
    
    extensão = '.pdf'
    pasta = 'static/'
    nome_antigo = 'static/recibo_assembleia_pronto.pdf'
    novo_nome = 'Recibo de' + ' ' + nome + extensão 
   

    if os.path.exists(novo_nome):
        os.remove(novo_nome)

    os.rename(nome_antigo, novo_nome)
    
    caminho_arquivo = novo_nome
      
    try:
        response = FileResponse(open(caminho_arquivo, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(novo_nome)
        return response
    except Exception:
        return HttpResponseBadRequest('Erro ao baixar o arquivo')

        
    
    return render(request, 'templates/recibo_assembleia.html', {'formgerais':formgerais ,'formusuarios': formusuarios, 'gerais': gerais, 'usuarios': usuarios, })    