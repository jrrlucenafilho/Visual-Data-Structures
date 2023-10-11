class PilhaSeq:
    def __init__(self, TAM_MAX):
        self.TAM_MAX = TAM_MAX
        self.dados = []

    def vazia(self):
        return len(self.dados) == 0

    def cheia(self):
        return len(self.dados) == self.TAM_MAX

    def tamanho(self):
        return len(self.dados)

    def top(self):
        if self.vazia():
            return -1
        return self.dados[-1]

    def push(self, valor):
        if self.cheia():
            return False
        self.dados.append(valor)
        return True

    def pop(self):
        if self.vazia():
            return -1
        return self.dados.pop()