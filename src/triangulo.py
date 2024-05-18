import math


def area_triangulo(a, b, c):
    """
    Calcula el área de un triángulo dados sus tres lados usando la fórmula de Herón.

    Parámetros:
    a (float): Longitud del primer lado.
    b (float): Longitud del segundo lado.
    c (float): Longitud del tercer lado.

    Retorna:
    float: Área del triángulo.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Los lados deben ser números positivos.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Los lados no forman un triángulo válido.")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def main():
    try:
        a = float(input("Ingrese el primer lado del triángulo: "))
        b = float(input("Ingrese el segundo lado del triángulo: "))
        c = float(input("Ingrese el tercer lado del triángulo: "))
        area = area_triangulo(a, b, c)
        print(f"El área del triángulo con lados {a}, {b} y {c} es: {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
