"""
O desafio para o dia de hoje é implementar um sistema de gerenciamento de
pacientes em um hospital usando listas simplesmente encadeadas.

Cada paciente deve ter um nome, um número de identificação e o estado de saúde
atual do paciente, como "estável", "em tratamento intensivo", "em estado
crítico", entre outros.

O sistema deve permitir adicionar novos pacientes, remover pacientes e listar
todos os pacientes em ordem de chegada.
"""

# Definindo a classe Paciente para estar representando o nó da lista
class Paciente:
    def __init__(self, id, nome, estado_saude):
        self.id = id
        self.nome = nome
        self.estado_saude = estado_saude
        self.proximo_paciente = None

# Definindo a classe ListaDePacientes para representar a lista simplesmente encadeada.
class ListaDePacientes:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_paciente(self, id, nome, estado_saude):
        novo_paciente = Paciente(id, nome, estado_saude)
        
        # Se a lista estiver vazia, o novo paciente é adicionado como cabeça e cauda da lista
        if self.head is None:
            self.head = novo_paciente
            self.tail = novo_paciente
        else:
            # Caso contrário, o paciência é inserido ao final da lista.
            self.tail.proximo_paciente = novo_paciente
            self.tail = novo_paciente

    def remover_paciente(self, id):
        # Se a lista estiver vazia, não há o que remover e lavanta um erro.
        if self.head is None:
            raise ValueError('Não há pacientes na lista.')
        elif self.head.id == id:
            # Se o paciente que será removido for a cabeça da lista, só atualizaremos o ponteiro para o próximo paciente.
            self.head = self.head.proximo_paciente
            if self.head is None:
                # Se a lista ficar vazia, é atualizado a cauda.
                self.tail = None
            return
        else:
            # Caso contrário, toda a lista é percorrida até encontrar o paciente a ser removido.
            paciente_atual = self.head
            while paciente_atual.proximo_paciente:
                # Quando encontramos o paciente, atualizamos o ponteiro do paciente anterior para o próximo paciente.
                if paciente_atual.proximo_paciente.id == id:
                    paciente_atual.proximo_paciente = paciente_atual.proximo_paciente.proximo_paciente
                    # Se o paciente removido for o último, apenas atualiza a cauda
                    if paciente_atual.proximo_paciente is None:
                        self.tail = paciente_atual
                        return
                paciente_atual = paciente_atual.proximo_paciente

    def imprimir(self):
        if self.head is None:
            raise ValueError('Não há pacientes na lista.')
        else:
            paciente_atual = self.head

            while paciente_atual:
                print(
                    f'ID: {paciente_atual.id}, Nome: {paciente_atual.nome}, '
                    f'Estado de Saúde: {paciente_atual.estado_saude}'
                )
                paciente_atual = paciente_atual.proximo_paciente


if __name__ == "__main__":
    lista = ListaDePacientes()

    lista.inserir_paciente(1, 'Eduardo', 'Estável')
    lista.inserir_paciente(2, 'Carlos', 'Crítico')
    lista.inserir_paciente(3, 'Giovanna', 'Tratamento intensivo')
    lista.imprimir()
    print('\nApós remoção.\n')
    lista.remover_paciente(2)
    lista.remover_paciente(4)
    lista.imprimir()
