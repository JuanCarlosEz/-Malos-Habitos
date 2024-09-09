def Area_rectangulo(a, b):
    area = a * b
    return area

def Area_triangulo(b, h):
    area = 0.5 * b * h
    return area

def main():
    print("MENU")
    print("1.Area del rectangulo")
    print("2.Area del triangulo")
    print("3.salir")
    opcion=int(input("Escriba una opcion (1-3) :"))

    if opcion == "1":
        BaseRectangulo = float(input("Ingresa la base del rectángulo: "))
        AlturaRectangulo = float(input("Ingresa la altura del rectángulo: "))
        rect_area = Area_rectangulo(BaseRectangulo, AlturaRectangulo)
        print("Área del rectángulo:", rect_area)

    elif opcion == "2":
        BaseTriangulo = float(input("Ingresa la base del triángulo: "))
        AlturaTriangulo = float(input("Ingresa la altura del triángulo: "))
        tri_area = Area_triangulo(BaseTriangulo, AlturaTriangulo)
        print("Área del triángulo:", tri_area)

    elif opcion == "3":
         exit(0)

if __name__ == "__main__":
    main()
