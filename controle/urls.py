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
    path('congresso_sexta/', views.congresso_sexta),
    path('deletar_gerais_congresso_sexta/', views.deletar_gerais_congresso_sexta),
    path('add_gerais_congresso_sexta/', views.add_gerais_congresso_sexta),
    path('editar_gerais_congresso_sexta/<int:id>', views.editar_gerais_congresso_sexta),
    path('recibo_congresso_sexta/<int:id>', views.recibo_congresso_sexta),
    path('organizar_congresso_sexta/', views.organizar_congresso_sexta),
    path('editar_lista_congresso_sexta/<int:id>', views.editar_lista_congresso_sexta),
    path('deletar_usuario_congresso_sexta/<int:id>', views.deletar_usuario_congresso_sexta),
    path('poltrona_congresso_sexta/<int:id>', views.poltrona_congresso_sexta),
    path('congresso_sabado/', views.congresso_sabado),
    path('deletar_gerais_congresso_sabado/', views.deletar_gerais_congresso_sabado),
    path('add_gerais_congresso_sabado/', views.add_gerais_congresso_sabado),
    path('editar_gerais_congresso_sabado/<int:id>', views.editar_gerais_congresso_sabado),
    path('recibo_congresso_sabado/<int:id>', views.recibo_congresso_sabado),
    path('organizar_congresso_sabado/', views.organizar_congresso_sabado),
    path('editar_lista_congresso_sabado/<int:id>', views.editar_lista_congresso_sabado),
    path('deletar_usuario_congresso_sabado/<int:id>', views.deletar_usuario_congresso_sabado),
    path('poltrona_congresso_sabado/<int:id>', views.poltrona_congresso_sabado),
    path('congresso_domingo/', views.congresso_domingo),
    path('deletar_gerais_congresso_domingo/', views.deletar_gerais_congresso_domingo),
    path('add_gerais_congresso_domingo/', views.add_gerais_congresso_domingo),
    path('editar_gerais_congresso_domingo/<int:id>', views.editar_gerais_congresso_domingo),
    path('recibo_congresso_domingo/<int:id>', views.recibo_congresso_domingo),
    path('organizar_congresso_domingo/', views.organizar_congresso_domingo),
    path('editar_lista_congresso_domingo/<int:id>', views.editar_lista_congresso_domingo),
    path('deletar_usuario_congresso_domingo/<int:id>', views.deletar_usuario_congresso_domingo),
    path('poltrona_congresso_domingo/<int:id>', views.poltrona_congresso_domingo),
    
    
   

]
    