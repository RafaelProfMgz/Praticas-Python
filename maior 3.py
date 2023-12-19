def maximo(a, b, c):
    maximo = a

    if b > maximo:
        maximo = b

    if c > maximo:
        maximo = c

    return maximo

def main():
    num1, num2, num3 = map(int, input("Digite três números: ").split())

    resultado = maximo(num1, num2, num3)
    print("O maior valor é:", resultado)

if __name__ == "__main__":
    main()