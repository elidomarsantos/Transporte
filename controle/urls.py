from django.urls import path

from . import views

urlpatterns = [

    path('', views.home),
    path('add_usuario/', views.add_usuario),
    path('lista_usuario/', views.lista_usuario),
    path('editar_lista/<int:id>', views.editar_lista),
    path('deletar_usuario/<int:id>', views.deletar_usuario),
    path('organizar/', views.organizar),
    path('gerais/', views.gerais),
    path('deletar_gerais/', views.deletar_gerais),
    path('add_gerais/', views.add_gerais),
    path('editar_gerais/<int:id>', views.editar_gerais),
    path('editar_poltrona/<int:id>', views.editar_poltrona),
   

]
    