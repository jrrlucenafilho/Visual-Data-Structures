# Importe a classe No (certifique-se de que ela esteja definida em outro lugar do seu código)
from No import No

# Defina a classe ListaEncadeadaSimples
class ListaEncadeadaSimples:
    # Construtor da classe
    def __init__(self):
        self.cabeca = None   # Inicializa a cabeça da lista como nula (lista vazia)
        self.n_elementos = 0 # Inicializa o número de elementos como 0

    # Verifica se a lista está vazia
    def esta_vazia(self):
        return self.n_elementos == 0

    # Retorna o tamanho da lista
    def tamanho(self):
        return self.n_elementos

    # Retorna o valor do elemento na posição 'pos' da lista
    def elemento(self, pos):
        if self.esta_vazia() or pos < 1 or pos > self.tamanho():
            return "Posição inválida ou lista vazia"

        aux = self.cabeca
        for i in range(1, pos):
            aux = aux.proximo

        return aux.conteudo

    # Retorna a posição do primeiro elemento com o valor 'dado' na lista
    def posicao(self, dado):
        if self.esta_vazia():
            return "Lista vazia"

        aux = self.cabeca
        cont = 1
        while aux is not None:
            if aux.conteudo == dado:
                return cont
            aux = aux.proximo
            cont += 1

        return "Valor não encontrado"

    # Insere um novo nó com o valor 'valor' no início da lista
    def insere_no_inicio(self, valor):
        novo_no = No()
        novo_no.conteudo = valor
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self.n_elementos += 1

    # Insere um novo nó com o valor 'valor' na posição 'pos' da lista
    def insere_no_meio(self, pos, valor):
        if pos < 1 or pos > self.tamanho() + 1:
            return "Posição inválida"

        if pos == 1:
            self.insere_no_inicio(valor)
            return True

        novo_no = No()
        novo_no.conteudo = valor
        aux = self.cabeca
        for i in range(1, pos - 1):
            aux = aux.proximo

        novo_no.proximo = aux.proximo
        aux.proximo = novo_no
        self.n_elementos += 1
        return True

    # Insere um novo nó com o valor 'valor' na posição 'pos' da lista
    def insere(self, pos, valor):
        if self.esta_vazia() and pos != 1:
            return "Lista vazia com posição inválida"

        if pos < 1 or pos > self.tamanho() + 1:
            return "Posição inválida"

        if pos == 1:
            self.insere_no_inicio(valor)
            return True
        else:
            return self.insere_no_meio(pos, valor)

    # Remove o primeiro nó da lista e retorna o valor removido
    def remove_do_inicio(self):
        if self.esta_vazia():
            return "Lista vazia"

        valor_removido = self.cabeca.conteudo
        self.cabeca = self.cabeca.proximo
        self.n_elementos -= 1
        return valor_removido

    # Remove o nó na posição 'pos' da lista e retorna o valor removido
    def remove_do_meio(self, pos):
        if pos < 1 or pos > self.tamanho():
            return "Posição inválida"

        if pos == 1:
            return self.remove_do_inicio()

        aux = self.cabeca
        for i in range(1, pos - 1):
            aux = aux.proximo

        no_removido = aux.proximo
        aux.proximo = no_removido.proximo
        self.n_elementos -= 1
        return no_removido.conteudo

    # Remove o nó na posição 'pos' da lista e retorna o valor removido
    def remove(self, pos):
        if self.esta_vazia():
            return "Lista vazia"

        if pos < 1 or pos > self.tamanho():
            return "Posição inválida"

        if pos == 1:
            return self.remove_do_inicio()
        else:
            return self.remove_do_meio(pos)

    # Retorna o valor do elemento na posição 'pos' da lista
    def busca_posicao(self, pos):
        if pos < 1 or pos > self.tamanho():
            return "Posição inválida"

        aux = self.cabeca
        for i in range(1, pos):
            aux = aux.proximo

        return aux.conteudo

    # Retorna uma lista de posições onde o valor 'valor' é encontrado na lista
    def busca_valor(self, valor):
        if self.esta_vazia():
            return []  # Retorna uma lista vazia se a lista está vazia

        aux = self.cabeca
        posicoes = []  # Inicializa uma lista para armazenar as posições

        posicao = 1  # Inicializa a posição como 1 (a primeira posição)

        while aux is not None:
            if aux.conteudo == valor:
                posicoes.append(posicao)  # Adiciona a posição onde o valor foi encontrado à lista
            aux = aux.proximo
            posicao += 1  # Incrementa a posição

        return posicoes  # Retorna a lista de posições onde o valor foi encontrado
