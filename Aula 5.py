#Aula 5 - Computational Thinking for Engineering

pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f"Insira a resposta da questão {questao}: ")
    if questao == 1 and resposta == "b":
        pontos += 1
    elif questao == 2 and resposta == "a":
        pontos += 1
    elif questao == 3 and resposta == "d":
        pontos += 1
    questao += 1
print(f"Nota final do Aluno: {pontos}")

n = 1
soma = 0
while n <= 10:
    x = float(input(f"Digite o {n}º número: "))
    soma = soma + x
    n += 1
print(f"Soma = {soma/(n-1):.2f}")

# Listas - Arrays

lista = [1, 2, 3, 4, 5]

i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1

lista = [1, 2, 3, 4, 5]

i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1
    lista.append(i)

deposit = float(input(f"Qual o valor do seu depósito inicial? "))
juros = float(input(f"Qual a taxa de juros? "))
mes = 1
depMes = 0

while mes <= 24:
    deposit = deposit + (deposit*(juros/100)) + depMes
    print(f"Valor polpança do {mes}º mês: R${deposit:.2f}")
    depMes = float(input("Deposito?"))
    mes += 1

soma = 0
while True:
    num = input(f"Digite: ")
    if num == "fim":
        break
    soma += float(num)
print(f"Resultado: {soma:.2f}")
