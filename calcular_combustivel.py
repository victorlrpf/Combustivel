#Inserir dados
print("Olá vamos calcular o seu consumo de combustivel")

carro = input("Qual o seu carro?  ")
km_rodados = int(input("Qual o número de quilometros rodados:  "))
quantidade = int(input("Quantidade de litros dp tanque:  "))

print("-=" * 20)

#Aplicando a logica
print('{} / {}' .format(km_rodados, quantidade))
consumo = km_rodados / quantidade

print("-=" * 20)

# Resultado
print('O consumo de combustivel do {}, foi de {}' .format(carro, consumo))