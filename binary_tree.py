from node import Node


class BinaryTree:

  def __init__(self):
    self.root = None

  def adicionar(self, value):
    node = Node(value)
    if self.root is None:
      self.root = node
    if value == self.root.value:
      return
    if value < self.root.value:
      if self.root.esquerda:
        self.root.esquerda.adicionar(value)
      else:
        self.root.esquerda = BinaryTree()
        self.root.esquerda.adicionar(value)
    if value > self.root.value:
      if self.root.direita:
        self.root.direita.adicionar(value)
      else:
        self.root.direita = BinaryTree()
        self.root.direita.adicionar(value)

  def min(self):
    if self.root.esquerda is None:
      return self.root.value
    return self.root.esquerda.min()

  def remove(self, num):
    if num < self.root.value:
      if self.root.esquerda:
        self.root.esquerda = self.root.esquerda.remove(num)
    elif num > self.root.value:
      if self.root.direita:
        self.root.direita = self.root.direita.remove(num)
    else:
      if self.root.esquerda is None and self.root.direita is None:
        return None

      min_val = self.root.direita.min()
      self.root.value = min_val
      self.root.direita = self.root.direita.remove(min_val)
    return self

  def preOrder(self):
    elements = []
    if self.root.esquerda:
      elements += self.root.esquerda.preOrder()
    elements.append(self.root.value)
    if self.root.direita:
      elements += self.root.direita.preOrder()
    return elements

  def inOrder(self):
    elements = []
    if self.root.value not in elements:
      elements.append(self.root.value)
    if self.root.esquerda:
      elements += self.root.esquerda.inOrder()
    if self.root.direita:
      elements += self.root.direita.inOrder()

    return elements

  def posOrder(self):
    elements = []
    if self.root:
      if self.root.esquerda:
        elements += self.root.esquerda.posOrder()
      if self.root.direita:
        elements += self.root.direita.posOrder()
      elements.append(self.root.value)
    return elements

  def search(self, val):
    if self.root.value == val:
      return True
    if val < self.root.value:
      if self.root.esquerda:
        return self.root.esquerda.search(val)
      else:
        False
    if val > self.root.value:
      if self.root.direita:
        return self.root.direita.search(val)
      else:
        False

  def printTree(self, alt=0):
    if self.root.direita:
      self.root.direita.printTree(alt + 1)
    print(' ' * 4 * alt + " ->" + str(self.root.value))
    if self.root.esquerda:
      self.root.esquerda.printTree(alt + 1)