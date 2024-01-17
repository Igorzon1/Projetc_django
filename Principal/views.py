from django.shortcuts import render,redirect, get_object_or_404
from .models import Cliente, Pedido
from .forms import ClienteForm

def home(request):
    clientes = Cliente.objects.order_by('-id_cliente')[:8]

    return render(request,'paginas/inicio.html',{'clientes': clientes})

def Adicionar_pedido(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        nome_produto = request.POST.get('nome_produto')
        quantidade = request.POST.get('quantidade')
        valor_unitario = request.POST.get('valor_unitario')

        cliente = Cliente.objects.get(pk=cliente_id)

        Pedido.objects.create(
            cliente=cliente,
            nome_produto=nome_produto,
            quantidade=quantidade,
            valor_unitario=valor_unitario,
            valor_total=float(quantidade) * float(valor_unitario)
        )

        ultimo_pedido = Pedido.objects.latest('id_pedido')

        return render(request,'paginas/confirmacao_pedido.html',{'ultimo_pedido':ultimo_pedido} )

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome is not None:
            cpf = request.POST.get('cpf')
            telefone = request.POST.get('telefone')
            residencia = request.POST.get('residencia')

            Cliente.objects.create(nome=nome, cpf=cpf, telefone=telefone, residencia=residencia)
            #return redirect('pagina_clientes')

    return render(request, 'paginas/confirmacao.html')

def pesquisar_clientes(request):
    query = ''
    if 'query' in request.GET:
        query = request.GET['query']
        # Lógica para filtrar clientes com base na pesquisa (pode ser mais complexa)
        clientes = Cliente.objects.filter(nome__icontains=query)
    else:
        clientes = Cliente.objects.all()

    return render(request, 'paginas/clientes.html', {'clientes': clientes, 'query': query})

def exibir_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request,'paginas/ver_pedidos.html',{'pedidos':pedidos})

def pesquisar(request):
    # Obter parâmetros de pesquisa da URL
    produto = request.GET.get('produto', '')
    cliente = request.GET.get('cliente', '')

    # Filtrar pedidos com base nos parâmetros de pesquisa
    pedidos = Pedido.objects.all()

    if produto:
        pedidos = pedidos.filter(nome_produto__icontains=produto)

    if cliente:
        pedidos = pedidos.filter(cliente__nome__icontains=cliente)

    # Restante da lógica para obter e processar os pedidos
    # ...

    return render(request, 'paginas/ver_pedidos.html', {'pedidos': pedidos})

def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('pesquisar_clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'paginas/editar_cliente.html', {'form': form, 'cliente': cliente})
