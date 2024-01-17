from django.contrib import admin
from .models import Cliente, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["id_cliente", "nome", "cpf", "telefone", "residencia"]

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["id_pedido", "cliente", "nome_produto", "quantidade", "valor_unitario", "valor_total", "data_compra", "data_atualizacao"]
