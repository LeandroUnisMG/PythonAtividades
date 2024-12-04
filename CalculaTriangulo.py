import math

def verificar_triangulo(a, b, c):
    
    if a < b + c and b < a + c and c < a + b:
        return True
    return False

def calcular_area(a, b, c):
    
    semiperimetro = (a + b + c) / 2
    area = math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c))
    return area

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if verificar_triangulo(a, b, c):
    area = calcular_area(a, b, c)
    print(f"Os valores formam um triângulo. A área é: {area:.2f}")
else:
    print(f"Os valores {a}, {b}, {c} não formam um triângulo.")
