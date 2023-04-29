from django.urls import path

from . import views

urlpatterns = [

    path('', views.home),
    path('inicial/', views.inicial),
    path('add_usuario/', views.add_usuario),
    path('lista_usuario/', views.lista_usuario),
    path('editar_lista/<int:id>', views.editar_lista),
    path('deletar_usuario/<int:id>', views.deletar_usuario),
    path('assembleia/', views.assembleia),
    path('deletar_gerais_assembleia/', views.deletar_gerais_assembleia),
    path('add_gerais_assembleia/', views.add_gerais_assembleia),
    path('editar_gerais_assembleia/<int:id>', views.editar_gerais_assembleia),
    path('recibo_assembleia/<int:id>', views.recibo_assembleia),
    path('organizar_assembleia/', views.organizar_assembleia),
    path('editar_lista_assembleia/<int:id>', views.editar_lista_assembleia),
    path('deletar_usuario_assembleia/<int:id>', views.deletar_usuario_assembleia),
    path('poltrona_assembleia/<int:id>', views.poltrona_assembleia),
   

]
    