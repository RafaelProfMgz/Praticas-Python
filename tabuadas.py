
def calcularTabuada(N):
    for i in range(1, N + 1):
        print(f"Tabuada do {i}:")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print()

def main():
    N = int(input("Digite um valor N para calcular a tabuada de 1 até N: "))
    calcularTabuada(N)

if __name__ == "__main__":
    main()



def calcularTabuada(N):
    print(f"Tabuada do {N}:")
    for i in range(1, 11):
            resultado =i   * N
            print(f"{i} x   {N} = {resultado}")

def main():
    N = int(input("Digite um valor N para calcular a tabuada de 1 até N: "))
    calcularTabuada(N)

if __name__ == "__main__":
    main()