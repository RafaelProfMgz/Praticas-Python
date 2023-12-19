import os  

def conversor():
    def hexadecimal_para_octal(hexadecimal):
        decimal = hexadecimal_para_decimal(hexadecimal)
        return oct(decimal)[2:]  

    def hexadecimal_para_binario(hexadecimal):
        decimal = hexadecimal_para_decimal(hexadecimal)
        return bin(decimal)[2:]  

    def hexadecimal_para_decimal(hexadecimal):
        return int(hexadecimal, 16)


    def decimal_para_octal(decimal):
        return oct(decimal)[2:]

    def decimal_para_binario(decimal):
        return bin(decimal)[2:]

    def decimal_para_hexadecimal(decimal):
        return hex(decimal)[2:]


    def binario_para_octal(binario):
        decimal = binario_para_decimal(binario)
        return oct(decimal)[2:] 

    def binario_para_hexadecimal(binario):
        decimal = binario_para_decimal(binario)
        return hex(decimal)[2:] 

    def binario_para_decimal(binario):
        return int(binario, 2)


    def octal_para_binario(octal):
        decimal = octal_para_decimal(octal)
        return bin(decimal)[2:] 

    def octal_para_hexadecimal(octal):
        decimal = octal_para_decimal(octal)
        return hex(decimal)[2:]

    def octal_para_decimal(octal):
        return int(octal, 8)


    def escolher_conversao():
        print("Escolha a conversão:")
        print("1. Hexadecimal para Octal")
        print("2. Hexadecimal para Binario") 
        print("3. Hexadecimal para Decimal")
        print("4. Decimal para Octal")
        print("5. Decimal para Binario") 
        print("6. Decimal para Hexadecimal")
        print("7. Binario para Octal")
        print("8. Binario para Hexadecimal") 
        print("9. Binario para Decimal")
        print("10. Octal para Binario")
        print("11. Octal para Hexadecimal") 
        print("12. Octal para Decimal")

        escolha = int(input("Digite o número da opção desejada: "))

        if escolha == 1:
            hexadecimal = input("Digite o valor hexadecimal: ")
            resultado = hexadecimal_para_octal(hexadecimal)
            

        elif escolha == 2:
            hexadecimal = input("Digite o valor hexadecimal pois é zé: ")
            resultado = hexadecimal_para_binario(hexadecimal)    
            

        elif escolha == 3:
            hexadecimal = input("Digite o valor hexadecimal: ")
            resultado = hexadecimal_para_decimal(hexadecimal)
            

        elif escolha == 4:
            decimal = int(input("Digite o valor decimal: "))
            resultado = decimal_para_octal(decimal)
            

        elif escolha == 5:
            decimal = int(input("Digite o valor decimal: "))
            resultado = decimal_para_binario(decimal)
            

        elif escolha == 6:
            decimal = int(input("Digite o valor decimal: "))
            resultado = decimal_para_hexadecimal(decimal)
            

        elif escolha == 7:
            binario = input("Digite o valor binário: ")
            resultado = binario_para_octal(binario)
            

        elif escolha == 8:
            binario = input("Digite o valor binário: ")
            resultado = binario_para_hexadecimal(binario)
            

        elif escolha == 9:
            binario = input("Digite o valor binário: ")
            resultado = binario_para_decimal(binario)
            
        elif escolha == 10:
            octal = input("Digite o valor octal: ")
            resultado = octal_para_binario(octal)


        elif escolha == 11:
            octal = input("Digite o valor octal: ")
            resultado = octal_para_hexadecimal(octal)
            

        elif escolha == 12:
            octal = input("Digite o valor octal: ")
            resultado = octal_para_decimal(octal)
            

        else:
            print("Opção inválida.")
            return

        print(f"Resultado: {resultado}")

    escolher_conversao()

def calculadora():

    def soma(num1, num2):
        return num1 + num2

    def subtracao(num1, num2):
        return num1 - num2

    def multiplicacao(num1, num2):
        return num1 * num2

    def divisao(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"

    def escolher_operacao(entrada):
        operacoes = {
            '+': soma,
            '-': subtracao,
            '*': multiplicacao,
            '/': divisao
        }
        
        partes = entrada.split()
        if len(partes) != 3:
            return "Entrada inválida"

        num1 = float(partes[0])
        operador = partes[1]
        num2 = float(partes[2])

        if operador in operacoes:
            resultado = operacoes[operador](num1, num2)
            return f"Resultado: {resultado}"
        else:
            return "Operador inválido"

    entrada = input("Digite a operação (exemplo: 2 + 2): ")
    resultado = escolher_operacao(entrada)
    print(resultado)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def escolha():
    
    while True:
            clear_screen()
            print("Escolha uma forma:")
            print("1. Conversor")
            print("2. Calculadora")
            print("3. Sair")

            escolha = int(input("Digite o número da operação desejada: "))
            
            if escolha == 1:
                conversor()
            elif escolha == 2:
                calculadora()
            elif escolha == 3:
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Escolha inválida. Por favor, escolha 1 para o Conversor, 2 para a Calculadora ou 3 para sair.")
            
            input("Pressione Enter para sair...")

escolha()