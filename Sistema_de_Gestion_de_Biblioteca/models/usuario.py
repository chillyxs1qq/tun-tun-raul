class Usuario:
    def __init__(self, id_usuario, nombre, apellido, email):
        self.id = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.estado = "activo"
        self.suspension_hasta = None

    # Métodos de acceso
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getEmail(self):
        return self.email

    def getEstado(self):
        return self.estado

    def getSuspensionHasta(self):
        return self.suspension_hasta

    # Métodos para modificar atributos
    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def setApellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def setEmail(self, nuevo_email):
        self.email = nuevo_email

    def setEstado(self, nuevo_estado):
        self.estado = nuevo_estado

    def setSuspensionHasta(self, fecha):
        self.suspension_hasta = fecha

    # Representación del usuario
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre} {self.apellido}, Email: {self.email}, Estado: {self.estado}"
