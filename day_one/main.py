"""
O desafio para o dia é implementar uma versão simplificada de uma lista de
compras usando arrays. A lista deve permitir adicionar novos itens, remover
itens e listar todos os itens.

Ao adicionar um novo item, o usuário deve inserir o nome do produto e a
quantidade desejada. Ao remover um item, o usuário deve especificar o nome do
produto. Por fim, ao listar todos os itens, a lista deve exibir o nome do
produto e a quantidade em um formato legível.
"""

# Definindo a classe de ListaDeCompras.


class ListaDeCompras:
    def __init__(self):
        self.itens = []
        self.quantidades = []

    # Adicionando itens ao array.
    def adicionar_item(self, item, quantidade):
        if item in self.itens:
            index = self.itens.index(item)
            self.quantidades[index] += quantidade
        else:
            self.itens.append(item)
            self.quantidades.append(quantidade)

    # Removendo os produtos do array de acordo com o seu nome.
    def remover_item(self, item):
        if item in self.itens:
            index = self.itens.index(item)
            self.itens.remove(item)
            del self.quantidades[index]
        else:
            raise ValueError('Item não encontrado na lista de compras.')

    # Impressão de todos os produtos da lista de compras.
    def listar_itens(self):
        if len(self.itens) != len(self.quantidades):
            raise ValueError(
                'As listas de itens e quantidades devem ter o mesmo tamanho.'
            )

        for item, quantidade in zip(self.itens, self.quantidades):
            print(f'Item: {item} | Quantidade: {quantidade}')


if __name__ == "__main__":
    lista = ListaDeCompras()

    lista.adicionar_item('Maçãs', 5)
    lista.adicionar_item('Biscoito', 3)
    lista.adicionar_item('Laranjas', 2)
    lista.adicionar_item('Pêssegos', 4)
    lista.adicionar_item('Café', 2)

    print('Lista de compras:')
    lista.listar_itens()

    print('\nRemovendo o item "Laranjas"...')
    lista.remover_item('Laranjas')

    print("\nLista de compras após a remoção:")
    lista.listar_itens()

    print('Removendo o item "Coalhada" que não existe na lista.')
    lista.remover_item('Coalhada')
