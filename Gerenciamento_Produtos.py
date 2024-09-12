import Dados_Produtos as ga

def main():
    while True:
        print("\n1. Adicionar produto")
        print("2. Visualizar produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Encerrar programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            ga.adicionar_produto()
        elif opcao == '2':
            ga.visualizar_produtos()
        elif opcao == '3':
            ga.atualizar_produto()
        elif opcao == '4':
            ga.remover_produto()
        elif opcao == '5':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Start programa
if __name__ == "__main__":
    main()