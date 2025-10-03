from datetime import datetime

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.__id = id_usuario
        self.__nombre = nombre
        self.__estado = "activo"
        self.__suspension_hasta = None

    # --- Getters ---
    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getEstado(self):
        return self.__estado

    def getSuspensionHasta(self):
        return self.__suspension_hasta

    # --- Setters ---
    def setNombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def setEstado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def setSuspensionHasta(self, fecha):
        self.__suspension_hasta = fecha

    # --- Utilidad ---
    def __str__(self):
        return f"Usuario(ID={self.__id}, Nombre={self.__nombre}, Estado={self.__estado}, SuspensionHasta={self.__suspension_hasta})"
