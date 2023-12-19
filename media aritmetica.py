
while True:
    entrada = input("Digite um valor inteiro positivo (ou um valor negativo para encerrar): ")
    
    if entrada == "":
        continue

    valor = int(entrada)
    
    if valor < 0:
        if quantidade_valores > 0:
            break  # Encerra o loop se um valor negativo for digitado e já houver valores positivos
    else:
        soma += valor
        quantidade_valores += 1

if quantidade_valores > 0:
    media = soma / quantidade_valores
    print(f"A média dos valores é: {media:.2f}")
