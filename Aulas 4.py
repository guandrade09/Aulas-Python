#Aula 4 - Computational Thinking for Engineering

import time

#While

# x = 1
# print(x)
# x = x + 1
# print(x)
# x = x + 1
# print(x)
#
# x = 1
# while x <= 3:
#     print(x)
#     x = x + 1
#
# x = 1
# while x <= 100:
#     print(x)
#     x = x + 1
#
# y = 10
# print("Contagem regressiva para lançamento do foguete.")
# while y > 0:
#     time.sleep(1)
#     print(y)
#     y = y - 1
# print("Fogo!")
#
# z = int(input("Insira um número: "))
# num = 0
#
# if z%2 == 0:
#
#     num = 0
#     while num <= z:
#         print(num)
#         num+=2
#         time.sleep(0.5)
#
# elif z%2 != 0:
#
#     num = 1
#     while num <= z:
#         print(num)
#         num+=2
#         time.sleep(0.2)

tabuada = int(input("Insira um número: "))
resultado = 0
vezes = 0

while resultado <= tabuada*10:
    print(f"{tabuada} X {vezes} = {resultado}")
    resultado = resultado + tabuada
    vezes += 1
    time.sleep(0.5)

