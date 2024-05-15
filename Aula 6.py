genesis = ["Gustavo", "Vinicius", "André", "Lucas", "Arthur"]

print(genesis)
print(genesis[2])
genesis.sort()
print(genesis)

n = [4, 2, 10, 6, 18, 0]
n.sort()
print(f"Usando sort: {n}")
n.sort(reverse=True)
print(f"Usando sort reverse: {n}")
x = len(n)
print(f"Usando len: {x}")
n.sort()
print(f"Usando n[3:6]: {n[3:6]}")
n.append([44, 66])
print(f"Usando append com dois elementos: {n}")
print(f"Usando lista dentro da lista: {n[6][1]}")
n.extend([14, 92])
print(f"Usando extend: {n}")
n.remove(2)
print(f"Usando remove: {n}")
n.clear()
print(f"Usando clear: {n}")
n.append(100)
print(f"Usando o append: {n}")
n.extend([8, 16, 74, 42])
n2 = n[:3]
n.sort()
n2.sort(reverse=True)
print(n)
print(n2)

v = n[3] + n[4]
print(v)
