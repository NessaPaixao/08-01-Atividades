numero = input("Digite seu número de celular:")

if len(numero) == "9" and numero[0] == "9":
    print("Número cadastrado com sucesso")

else:
    print("Número inválido! Digite novamente")