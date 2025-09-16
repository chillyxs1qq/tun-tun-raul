from Sistema_de_Gestion_de_Biblioteca.services.Cola import Cola

class Reserva:
    def __init__(self):
        self.__idmaterial = 0
        self.__colaSocios = []


    def encolar(self, idSocio):
        self.__colaSocios.append(idSocio)

    def desencolar(self):
        self.__colaSocios.pop(0)

    def verCola(self):
        return self.__colaSocios