from pelicula import Pelicula 

def main():
    # Crear tres objetos distintos
    p1 = pelicula(1"terstellar", 169, "Christopher Nolan")
    p2 = pelicula(2, "Pulp Fiction", 154, "Quentin Tarantino")
    p3 = pelicula(1, "Otra Interstellar", 169, "Nolan")

    # Mostrar información
    print(p1)
    print(p2)
    print(p3)

    # Préstamo
    print("\nPréstamos:")
    print(p1.prestar())
    print(p1.prestar())  # Segundo intento, ya estaba prestada

    # Devolución
    print("\nDevoluciones:")
    print(p1.devolver())
    print(p1.devolver())  # Segundo intento, ya estaba devuelta

    # Costo de reproducción
    print("\nCostos de reproducción:")
    print(p2.costo_reproduccion(50))
    print(p3.costo_reproduccion(60))

    # Comparación
    print("\nComparación de películas:")
    print("¿peli1 y peli2 son iguales?", p1 == p2)
    print("¿peli1 y peli3 son iguales?", p1 == p3)

if __name__ == "__main__":
    main()
