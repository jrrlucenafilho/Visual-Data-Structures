class FilaSeq:
    def __init__(self, TAM_MAX):
        # Inicialização da fila com tamanho máximo
        self.TAM_MAX = TAM_MAX
        self.dados = [0] * TAM_MAX
        self.inicio = 0
        self.fim = -1
        self.nElementos = 0

    def vazia(self):
        # Verifica se a fila está vazia
        return self.nElementos == 0

    def cheia(self):
        # Verifica se a fila está cheia
        return self.nElementos == self.TAM_MAX

    def tamanho(self):
        # Retorna o número de elementos na fila
        return self.nElementos

    def primeiro(self):
        # Retorna o primeiro elemento da fila, se não estiver vazia
        if self.vazia():
            return -1
        return self.dados[self.inicio]

    def insere(self, valor):
        # Insere um valor na fila
        if self.cheia():
            return False  # Retorna False se a fila estiver cheia
        self.fim = (self.fim + 1) % self.TAM_MAX  # Atualiza o índice de fim (com tratamento de circularidade)
        self.dados[self.fim] = valor
        self.nElementos += 1  # Incrementa o número de elementos na fila
        return True

    def remove(self):
        # Remove o primeiro elemento da fila
        if self.vazia():
            return -1  # Retorna -1 se a fila estiver vazia
        valor = self.dados[self.inicio]  # Valor a ser removido
        self.inicio = (self.inicio + 1) % self.TAM_MAX  # Atualiza o índice de início (com tratamento de circularidade)
        self.nElementos -= 1  # Decrementa o número de elementos na fila
        return valor  # Retorna o valor removido
