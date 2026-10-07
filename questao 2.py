class ControleEstoque:
    def __init__(self, dados_iniciais):
        self.estoque = {item["codigoProduto"]: item for item in dados_iniciais["estoque"]}
        self.movimentacoes = []

    def listar_produtos(self):
        print("\n" + "="*40)
        print("         ESTOQUE ATUAL DE PRODUTOS")
        print("="*40)
        for codigo, produto in self.estoque.items():
            print(f"Código: {codigo} | Produto: {produto['descricaoProduto']} | Qtde: {produto['estoque']}")
        print("="*40)

    def movimentar(self, id_movimentacao, codigo_produto, tipo, quantidade, descricao):
        produto = self.estoque[codigo_produto]
        
        if tipo.lower() == "entrada":
            produto["estoque"] += quantidade
        elif tipo.lower() == "saida":
            if produto["estoque"] < quantidade:
                print(f"\n[Erro] Estoque insuficiente! O produto '{produto['descricaoProduto']}' possui apenas {produto['estoque']} unidades.")
                return False
            produto["estoque"] -= quantidade
        else:
            print("\n[Erro] Tipo de movimentação inválido. Use 'entrada' ou 'saida'.")
            return False
        
        registro = {
            "id": id_movimentacao,
            "codigoProduto": codigo_produto,
            "produto": produto["descricaoProduto"],
            "tipo": tipo,
            "quantidade": quantidade,
            "descricao": descricao,
            "estoqueFinal": produto["estoque"]
        }
        self.movimentacoes.append(registro)
        
        print(f"\n[Sucesso] Movimentação #{id_movimentacao} realizada!")
        print(f"-> Produto: {produto['descricaoProduto']} ({tipo.upper()} de {quantidade} un.)")
        print(f"-> Descrição automática: {descricao}")
        print(f"-> Nova Quantidade em Estoque: {produto['estoque']} unidades\n")
        return True

dados_estoque = {
	"estoque": [
	  { "codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150 },
	  { "codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75 },
	  { "codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200 },
	  { "codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320 },
	  { "codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90 }
	]
}

if __name__ == "__main__":
    sistema = ControleEstoque(dados_estoque)
    contador_id = 1

    while True:
        sistema.listar_produtos()
        opcao = input("Deseja realizar uma movimentação? (s/n): ").strip().lower()
        if opcao == 'n':
            print("\nEncerrando o sistema de controle de estoque.")
            break
        elif opcao != 's':
            print("\n[Erro] Opção inválida. Digite 's' para sim ou 'n' para não.")
            continue
        
        try:
            codigo = int(input("Digite o código do produto: "))
            
            if codigo not in sistema.estoque:
                print(f"\n[Erro] O código informado não existe.\n")
                continue
            
            tipo = input("Digite o tipo de movimentação ('entrada' ou 'saida'): ").strip().lower()
            
            if tipo == "entrada":
                descricao = "Compra de reposição"
            elif tipo == "saida":
                descricao = "Venda balcão"
            else:
                print("\n[Erro] Tipo inválido. Digite exatamente 'entrada' ou 'saida'.\n")
                continue
            
            quantidade = int(input("Digite a quantidade: "))
            
            sistema.movimentar(contador_id, codigo, tipo, quantidade, descricao)
            contador_id += 1
            
        except ValueError:
            print("\n[Erro] Entrada inválida. Certifique-se de digitar números inteiros para o código e a quantidade.\n")
