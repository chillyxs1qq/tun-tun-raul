class Reserva:
    def __init__(self, idmaterial):
        self.__idmaterial = idmaterial
        self.__colaSocios = []


    def encolar(self, idSocio):
        self.__colaSocios.append(idSocio)

    def desencolar(self):
        self.__colaSocios.pop()