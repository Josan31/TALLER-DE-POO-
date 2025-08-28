class Libro:
    def __init__(self, idLibro, titulo, autor):
        self.idLibro = idLibro
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"Libro '{self.titulo}' devuelto.")


class Prestamo:
    def __init__(self, idPrestamo, fechaInicio, fechaFin, usuario, ):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.estado = "Activo"
        self.usuario = usuario

    def crearPrestamo(self, libro):
        libro.prestar()
        print(f"Préstamo {self.idPrestamo} creado para {self.usuario.nombre}.")

    def cerrarPrestamo(self, libro):
        self.estado = "Cerrado"
        libro.devolver()
        print(f"Préstamo {self.idPrestamo} cerrado.")


class Usuario:
    def __init__(self, idUsuario, nombre, correo, telefono):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def solicitarPrestamo(self, libro, prestamo):
        prestamo.crearPrestamo(libro)

    def devolverLibro(self, libro, prestamo):
        prestamo.cerrarPrestamo(libro)

    def mostrarInfo(self):  # Polimorfismo
        print(f"Usuario: {self.nombre}, correo: {self.correo}")


class Bibliotecario(Usuario):  # Herencia
    def __init__(self, idEmpleado, nombre, apellido):
        self.idEmpleado = idEmpleado
        self.nombre = nombre
        self.apellido = apellido

    def registrarLibro(self, idLibro, titulo, autor):
        print(f"Libro '{titulo}' registrado por {self.nombre} {self.apellido}.")
        return Libro(idLibro, titulo, autor)

    def eliminarLibro(self, libro):
        print(f"Libro '{libro.titulo}' eliminado por {self.nombre} {self.apellido}.")

    def mostrarInfo(self):  # Polimorfismo (método redefinido)
        print(f"Bibliotecario: {self.nombre} {self.apellido}, ID: {self.idEmpleado}")

biblio = Bibliotecario("001", "Carlos", "Rodriguez")
libro1 = biblio.registrarLibro("10", "Cien años de soledad", "Alguien")

usuario1 = Usuario("001", "Juan", "juan@gmail.com", "3152639875")
prestamo1 = Prestamo("01", "2020-07-23", "2020-08-25", usuario1)

usuario1.solicitarPrestamo(libro1, prestamo1)
usuario1.devolverLibro(libro1, prestamo1)

# Ejemplo de polimorfismo
usuario1.mostrarInfo()
biblio.mostrarInfo()