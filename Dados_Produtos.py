#lista para armazenar os produtos
produtos = []

total_produtos = 0.0

# Adicionar Produto
def adicionar_produto():
    global total_produtos
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    valor_unitario = float(input("Digite o valor unitário: "))
    total_produto = quantidade * valor_unitario
    
    produto = {
        'produto': nome,
        'quantidade': quantidade,
        'valor': valor_unitario,
        'total': total_produto
    }
    
    produtos.append(produto)
    total_produtos += total_produto
    print(f"Produto '{nome}' adicionado com sucesso!")


# Ver a lista de produtos
def visualizar_produtos():
    if produtos:
        print("\nLista de produtos:")
        for p in produtos:
            print(f"Produto: {p['produto']}, Quantidade: {p['quantidade']}, "
                  f"Valor unitário: R${p['valor']:.2f}, Total: R${p['total']:.2f}")
        print(f"\nValor total de todos os produtos: R${total_produtos:.2f}")
    else:
        print("Nenhum produto na lista.")


# Atualizar um produto
def atualizar_produto():
    global total_produtos
    nome = input("Digite o nome do produto a ser atualizado: ")
    for p in produtos:
        if p['produto'] == nome:
            total_produtos -= p['total']  # Remove o valor antigo do total
            novo_nome = input("Digite o novo nome do produto (ou deixe em branco para manter): ") or p['produto']
            nova_quantidade = int(input(f"Digite a nova quantidade para '{p['produto']}' (ou o valor atual: {p['quantidade']}): ") or p['quantidade'])
            novo_valor = float(input(f"Digite o novo valor unitário para '{p['produto']}' (ou o valor atual: {p['valor']}): ") or p['valor'])
            
            p['produto'] = novo_nome
            p['quantidade'] = nova_quantidade
            p['valor'] = novo_valor
            p['total'] = nova_quantidade * novo_valor
            
            total_produtos += p['total']  # Adiciona o novo valor atualizado
            print(f"Produto '{nome}' atualizado com sucesso!")
            return
    print(f"Produto '{nome}' não encontrado.")



#Remover um produto
def remover_produto():
    global total_produtos
    nome = input("Digite o nome do produto a ser removido: ")
    for p in produtos:
        if p['produto'] == nome:
            total_produtos -= p['total']
            produtos.remove(p)
            print(f"Produto '{nome}' removido com sucesso!")
            return
    print(f"Produto '{nome}' não encontrado.")


