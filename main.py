# Exercicio 1
# (A)
n = int(input("Digite um valor para n: "))
S = 10

if n == 1:
    resultado = S
else:
    for i in range(2, n + 1):
        S = S(n - 1) + 10
    resultado = S

print("S({}) = {}".format(n, resultado))

# -----------------------------------------------------
# (B)
n = int(input("Digitr o valor desejado para n:"))
a = 2

if n == 1:
    resultado = a

else:
    for i in range(2, n + 1):
        a = (n ** -1)
        resultado = a
print("S({}) = {}".format(n, resultado))
# -----------------------------------------------------
# (C)
n = int(input("Digite o numero desejado:"))
b = 1

if n == 1:
    resultado = b
else:
    for i in range(2, n + 1):
        b = b + i ** 2
        resultado = b

print("B({}) = {}".format(n, resultado))
# -----------------------------------------------------
# (D)
n = int(input("Digite o número desejado:"))
p = 1
if n == 1:
    resultado = p
else:
    for i in range(2, n + 1):
        p = i ** 2 * p + i - 1
        resultado = p
print("P({}) = {}".format(n, resultado))
# ----------------------------------------------------
# (E)
n = int(input("Digite o número desejado:"))
d1 = 3
d2 = 5

if n == 1:
    resultado = d1
elif n == 2:
    resultado = d2
else:
    for i in range(3, n + 1):
        d3 = (i - 1) * d2 + (i - 2) * d1
        d1, d2 = d2, d3
        resultado = d3

print("D({}) = {}".format(n, resultado))
# -----------------------------------------------------
# (F)
n = int(input("Digite o número desejado:"))
w1 = 2
w2 = 5

if n == 1:
    resultado = w1
elif n == 2:
    resultado = w2
else:
    for i in range(3, n + 1):
        w1, w2 = w2, w1 * w2
    resultado = w2

print("W({}) = {}".format(n, resultado))
# -----------------------------------------------------
# (G)
n = int(input("Digite o número desejado:"))
t1 = 1
t2 = 2
t3 = 3

if n == 1:
    resultado = t1
elif n == 2:
    resultado = t2
elif n == 3:
    resultado = t3
else:
    for i in range(4, n + 1):
        t4 = (i - 1) + 2 * (i - 2) + 3 * (i - 3)
        t1, t2, t3 = t2, t3, t4
        resultado = t4

print("T({}) = {}".format(n, resultado))

# -----------------------------------------------------
# Exercicio 2

a = float(input("Digite o termo inicial (a): "))
r = float(input("Digite a razão (r): "))
n = int(input("Digite o valor de n: "))

termo = a

if n == 1:
    resultado = a
else:
    for i in range(2, n + 1):
        termo *= r

    resultado = termo

print(f"O {n}-ésimo termo da progressão geométrica é {resultado}")


# -----------------------------------------------------
# Exercicio 3

def perT(numero):
    if numero == 2:
        return True
    if numero < 2:
        return False
    return (perT(numero - 3) or perT(numero // 2))


numeros = [6, 7, 19, 12]

for numero in numeros:
    if perT(numero):
        print(f'{numero} pertence em T')
    else:
        print(f'{numero} não pertence em T')


# -----------------------------------------------------
# Exercicio 4

def perM(n, M):
    if n in M:
        return True
    for m in M:
        if m != 1 and n % m == 0:
            return perM(n // m, M)
    return False


M = {2, 3}
numeros = [6, 9, 16, 21, 26, 54, 72, 218]

for numero in numeros:
    if perM(numero, M):
        print(f"'{numero}' pertence em M")
    else:
        print(f"'{numero}' não pertence em M")


# ----------------------------------------------------
# Exercicio 5

def perS(cadeia):
    if cadeia == "a":
        return True
    if cadeia == "b":
        return True
    if cadeia.startswith("a") and perS(cadeia[1:]):
        return True
    if cadeia.startswith("b") and perS(cadeia[1:]):
        return True
    return False


cadeias = ["a", "ab", "aba", "aaab", "bbbbb"]

for cadeia in cadeias:
    if perS(cadeia):
        print(f'"{cadeia}" pertence em S')
    else:
        print(f'"{cadeia}" não pertence em S')


# -----------------------------------------------------
# Exercicio 6

def perW(cadeia):
    if cadeia in ['a', 'b', 'c']:
        return True
    elif len(cadeia) >= 3 and cadeia[0] == 'a' and cadeia[-1] == 'c':
        return perW(cadeia[1:-1])
    else:
        return False


cadeias = ['a(b)c', 'a(a(b)c)c', 'a(abc)c', 'a(a(a(a)c)c)c', 'a(aacc)c']

for cadeia in cadeias:
    if perW(cadeia):
        print(f"'{cadeia}' pertence em W")
    else:
        print(f"'{cadeia}' não pertence em W")


# ----------------------------------------------------
# Exercicio 7

def gerar_String_binaria(n, current_string="1"):
    if n == 0:
        print(current_string)
    else:
        gerar_String_binaria(n - 1, "0" + current_string + "0")
        gerar_String_binaria(n - 1, "0" + current_string)
        gerar_String_binaria(n - 1, current_string + "0")


n = int(input("Digite um numero inteiro"))
gerar_String_binaria(n)

# ------------------------------------------------------
# Exercicio 9

termo = int(input("Digite qual termo que é desejado "))
variavel = 0
valoradd = 0
for i in range(termo):
    valoradd = valoradd + 1
    variavel = variavel + valoradd

print(variavel)

# -----------------------------------------------------
# Eercicio 10 a)
contador = 0
horas = int(input("Quantas horas voce quer saber?"))
p_inicial = 50000

for i in range(horas):
    p_final = p_inicial * 3 ** horas
print(f"O valor final depois de {horas} horas é {p_final}")

# b)
contador = 0
p_inicial = 50000
p_final = p_inicial

while p_final < 200000:
    p_final *= 3
    contador += 1

print(f"Foi excedido a partir da leitura {contador}. O valor final é {p_final}")