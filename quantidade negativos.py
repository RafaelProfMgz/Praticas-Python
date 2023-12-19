
# Inicializamos uma variável para contar os valores negativos
quantidade_negativos = 0

# Loop para ler 5 valores
for i in range(8):
    valor = float(input(f"Digite o {i+1}º valor: "))  # Lê o valor como um número decimal
    
    # Verifica se o valor é negativo
    if valor < 0:
        quantidade_negativos += 1

# Mostra a quantidade de valores negativos
print(f"A quantidade de valores negativos é: {quantidade_negativos}")



import random

# Inicializamos uma variável para contar os valores negativos
quantidade_negativos = 0

# Loop para ler 5 valores aleatórios
for i in range(5):
    valor = random.randint(-100, 100)  # Gera um número aleatório entre -100 e 100
    
    # Verifica se o valor é negativo
    if valor < 0:
        quantidade_negativos += 1

# Mostra a quantidade de valores negativos
print(f"A quantidade de valores negativos é: {quantidade_negativos}")


