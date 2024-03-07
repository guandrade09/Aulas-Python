#Aula 2 - Computational Thinking for Engineering

print("Hello World!")

#Exercício 1

print("Gustavo Andrade de Sousa")

#Exercício 2

num_1 = 5
num_2 = 3
print(num_1)
print(num_2)
print(type(num_1))
print(type(num_2))
print("a + b")
print(num_1+num_2)

print("2a * 3b")
print(2*num_1*3*num_2)

#Exercício 3

num_3 = int(input("Digite o primeiro número: "))
num_4 = int(input("Digite o segundo número: "))
num_5 = int(input("Digite o terceiro número: "))

soma = num_3 + num_4 + num_5

print("Resultado:", soma)


pi = 3.14159
print(f"número: {pi:.2f}")

pi = 3.14159
print('número: {:.3f}'.format(pi))

pi = 3.14159
print("número: %.2f." %pi)

sqr = float
print("Raiz de 2 = ", float(round(2**(1/2), 4)))

d = True
print(d)
print(type(d))

nota = float(input("Coloque sua média: "))
freq = float(input("Coloque sua frequência: "))
media = 6

if nota >= 6 and freq >= 75:
    print("Aprovado! :)")
else:
    print("Reprovado. :(")

