from node import Node


class BinaryTree:

  def __init__(self):
    self.root = None

  def adicionar(self, value):
    node = Node(value)
    if self.root is None:
      self.root = node
    elif value < self.root.value:
      if self.root.esquerda is None:
        self.root.esquerda = BinaryTree()
        self.root.esquerda.adicionar(value)
      else:
        self.root.esquerda.adicionar(value)
    elif value > self.root.value:
      if self.root.direita is None:
        self.root.direita = BinaryTree()
        self.root.direita.adicionar(value)
      else:
        self.root.direita.adicionar(value)

      
    

  def pre_ordem(self):
    nos = 2**self.altura() - 1
    aux = self
    value = str(aux.root.value)
      
    return value

  def remove():
    return

  def show(self):
    aux = self
    print("[", end='')
    print(aux.root.value, end='')
    print("]")
    while (aux.root.esquerda is not None):
      aux = aux.root.esquerda
      print("[", end='')
      print(aux.root.value, end='')
      print("]")

  def altura(self):
    alt = 1
    while (self.root.direita != None or self.root.esquerda != None):
        while (self.root.direita != None):
            self = self.root.direita
            alt += 1 
        while (self.root.esquerda != None):
            self = self.root.esquerda
            alt += 1
    return alt
      