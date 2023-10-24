from No import No
ROOT = "root"

# classe arvore
class ABP:
    def __init__(self):
        self.lista_ordem = []
        self.raiz = None
        
    def limpar_arvore(self):
        self.raiz = None
        return True

    def verifica_vazia(self):
        return self.raiz is None


    def inserir(self, dado):
        novo_no = No(dado)

        if self.verifica_vazia():
            self.raiz = novo_no
            return True

        x = self.raiz
        posicao = None

        while (x != None):
            posicao = x

            if (dado == x.dado):
                return False

            if (dado < x.dado):
                x = x.esquerda
            else:
                x = x.direita

        if (dado < posicao.dado):
            posicao.esquerda = novo_no
        else:
            posicao.direita = novo_no

        return True

    # busa por um elemento na arvore
    def buscar(self, no_busca, dado):

        if (no_busca == None):
            return None

        if (dado == no_busca.dado):
            return no_busca

        if (dado < no_busca.dado):
            return self.buscar(no_busca.esquerda, dado)
        else:
            return self.buscar(no_busca.direita, dado)

    # busca o menor dado
    def menor_valor(self, no=ROOT):

        if no == ROOT:
            no = self.raiz

        while no.esquerda != None:
            no = no.esquerda
        return no.dado

    # busca o maior dado
    def maior_valor(self, no=ROOT):

        if no == ROOT:
            no = self.raiz

        while no.direita != None:
            no = no.direita
        return no.dado

    # remove um elemento
    def remover(self, dado, no_remover=ROOT):

        if  self.verifica_vazia() == True:
            return False

        no_pai = None
        if no_remover == ROOT:
            no_remover = self.raiz

        while True:
            if dado < no_remover.dado:
                no_pai = no_remover
                no_remover = no_remover.esquerda
            elif dado > no_remover.dado:
                no_pai = no_remover
                no_remover = no_remover.direita
            elif dado == no_remover.dado:
                break
            elif no_remover == None:
                return False

        if no_remover.esquerda == None and no_remover.direita == None:
            if no_pai is None:
                self.raiz = None
            elif no_pai.esquerda == no_remover:
                no_pai.esquerda = None
            elif no_pai.direita == no_remover:
                no_pai.direita = None
        elif no_remover.esquerda == None:
            if no_pai == None:
                self.raiz = no_remover.direita
            elif no_pai.esquerda == no_remover:
                no_pai.esquerda = no_remover.direita
            elif no_pai.direita == no_remover:
                no_pai.direita = no_remover.direita
        elif no_remover.direita == None:
            if no_pai == None:
                self.raiz = no_remover.esquerda
            elif no_pai.esquerda == no_remover:
                no_pai.esquerda = no_remover.esquerda
            elif no_pai.direita == no_remover:
                no_pai.direita = no_remover.esquerda
        else:
            substituto_pai = no_remover
            substituto = no_remover.direita
            while substituto.esquerda is not None:
                substituto_pai = substituto
                substituto = substituto.esquerda
            if substituto_pai != no_remover:
                substituto_pai.esquerda = substituto.direita
            else:
                substituto_pai.direita = substituto.direita
            no_remover.dado = substituto.dado
        return no_remover

    # salva os elementos pre_ordem em uma lista
    def pre_ordem(self):
        self.lista_ordem = resultado = []
        self._pre_ordem_(self.raiz, resultado)

    def _pre_ordem_(self, no, resultado):
        if no:
            resultado.append(no.dado)
            self._pre_ordem_(no.esquerda, resultado)
            self._pre_ordem_(no.direita, resultado)

    # salva os elementos pos_ordem em uma lista, usa a função posterior como auxiliadora
    def pos_ordem(self):
        self.lista_ordem = resultado = []
        self._pos_ordem_(self.raiz, resultado)

    def _pos_ordem_(self, no, resultado):
        if no:
            self._pos_ordem_(no.esquerda, resultado)
            self._pos_ordem_(no.direita, resultado)
            resultado.append(no.dado)

    # salva os elementos in-ordem em uma lista, usa a função posteriror como auxiliadora
    def in_ordem(self):
        self.lista_ordem = resultado = []
        self._in_ordem_(self.raiz, resultado)

    def _in_ordem_(self, no, resultado):
        if no:
            self._in_ordem_(no.esquerda, resultado)
            resultado.append(no.dado)
            self._in_ordem_(no.direita, resultado)

    # retorna a lista
    def retorna_lista(self):
        return self.lista_ordem
