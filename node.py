class Node:

    def __init__(self, value, direita = None, esquerda = None, cima = None):
        self.value = value
        self.direita = direita
        self.esquerda = esquerda

    def setDireita(self, direita):
        self.direita = direita

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda

    def showEsq(self):
      return self.esquerda.value
        