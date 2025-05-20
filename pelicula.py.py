#Kevin

class pelicula:
    # Constructor vacío y constructor con valores por defecto
    def __init__(self, codigo=0, titulo="", duracion=0, director="", prestada=False):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__duracion = duracion
        self.__director = director
        self.__prestada = prestada

    # Getters
    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_duracion(self):
        return self.__duracion

    def get_director(self):
        return self.__director

    def get_prestada(self):
        return self.__prestada

    # Setters
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def set_director(self, director):
        self.__director = director

    def set_prestada(self, prestada):
        self.__prestada = prestada

    # Método prestar
    def prestar(self):
        if not self.__prestada:
            self.__prestada = True
            return "La película ha sido prestada."
        else:
            return "La película ya estaba prestada."

    # Método devolver
    def devolver(self):
        if self.__prestada:
            self.__prestada = False
            return "La película ha sido devuelta."
        else:
            return "La película no estaba prestada."

    # Método costo_reproduccion
    def costo_reproduccion(self, tarifa_por_minuto):
        costo = self.__duracion * tarifa_por_minuto
        return f"El costo de reproducción es: ${costo:.2f}"

    # Método __str__
    def __str__(self):
        estado = "está prestada" if self.__prestada else "no está prestada"
        return (f"La película {self.__codigo} titulada \"{self.__titulo}\" dirigida por "
                f"{self.__director} dura {self.__duracion} minutos y {estado}.")

    # Método __eq__
    def __eq__(self, otra):
        if isinstance(otra, pelicula):
            return self.__codigo == otra.get_codigo()
        return False
if __name__ == "__main__":
    p1 = pelicula(1, "Interstellar", 169, "Christopher Nolan")
    p2 = pelicula(2, "Pulp Fiction", 154, "Quentin Tarantino")
    p3 = pelicula(1, "Otra Interstellar", 169, "Nolan")

    print(p1)
    print(p2)

    print(p1.prestar())
    print(p1.prestar())
    print(p1.devolver())

    print(p2.costo_reproduccion(30))

    print("¿p1 y p3 son la misma película?", p1 == p3)


