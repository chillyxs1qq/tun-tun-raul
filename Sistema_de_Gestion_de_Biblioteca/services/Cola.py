from collections import deque

class Cola:
    def __init__(self):
        self.__items = deque()

    def estaVacia(self):
        return len(self.__items) == 0

    def encolar(self, item):
        self.__items.append(item)

    def desencolar(self):
        if self.estaVacia():
            raise IndexError("La cola está vacía")
        return self.__items.popleft()

    def verFrente(self):
        if self.estaVacia():
            raise IndexError("La cola está vacía")
        return self.__items[0]

    def tamanio(self):
        return len(self.__items)

    def verFinal(self):
        if self.estaVacia():
            raise IndexError("La cola está vacía")
        return self.__items[-1]

    def limpiar(self):
        self.__items.clear()

    def contiene(self, item):
        return item in self.__items

    def clonar(self):
        nuevaCola = Cola()
        nuevaCola.__items = self.__items.copy()
        return nuevaCola

    def invertir(self):
        self.__items.reverse()

    def toLista(self):
        return list(self.__items)

    def encolarFrente(self, item):
        self.__items.appendleft(item)
