#  Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

numeros = [int(input(f"digite o número {i + 1}: ")) 
           for i in range(5)]

for i, num in enumerate(numeros):
    print(f"posição {i}: {num}")
