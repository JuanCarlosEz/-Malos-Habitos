def calcular(a, b, c):
    res = a * b + c
    return res

if __name__=="__main__":
    x=float(input("Ingrese el valor de x:"))
    y = float(input("Ingrese el valor de y:"))
    z = float(input("Ingrese el valor de z:"))
    Resultado=calcular(x,y,z)
    print(f"El resultado de la operacion es {Resultado}")
