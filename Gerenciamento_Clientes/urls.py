
from django.contrib import admin
from django.urls import path
from Principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('Clintes/',views.pesquisar_clientes,name='pesquisar_clientes'),
    path('pedido/',views.Adicionar_pedido,name= 'pedido' ),
    path('verpedido/',views.exibir_pedidos,name='verpedido'),
    path('pesquisar_pedidos/',views.pesquisar, name='pesquisar'),
    path('editar_cliente/<int:id_cliente>/', views.editar_cliente, name='editar_cliente')
]
