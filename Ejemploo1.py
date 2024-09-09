def multiplicacion(multiplicando, multiplicador):
    producto = multiplicando * multiplicador
    return producto


if __name__ == "__main__":
    multiplicando = float(input("Mul1: "))
    multiplicador = float(input("Mul2: "))
    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} *{multiplicador} ={resultado}")
