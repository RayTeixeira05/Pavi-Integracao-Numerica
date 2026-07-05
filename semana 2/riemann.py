import math

#Função a ser integrada
def f(x):
    return math.exp(x)  #A primitiva de exp(x) = exp(x)

#Implementação da Soma de Riemann
def riemann(f, a, b, n):

    dx = (b - a) / n

    soma = 0

    for i in range(n):
        x = a + i * dx
        soma += f(x)

    return soma * dx

#Intervalos
a = 0
b = 1

#Valor exato da integral
valor_exato = math.e - 1         #∫0 1 ​ex dx= e(x) ​0|1 ​= e(1) − e(0) = e - 1


#Valores de n
valores_n = [10, 100, 1000]

print(f"Valor exato = {valor_exato:.15f}\n")

#Produz uma tabela organizada
print(" n    Valor Aproximado      Valor Exato         Erro Absoluto")
print("-"*67)
for n in valores_n:
    aproximado = riemann(f, a, b, n)
    erro = abs(valor_exato - aproximado)
    print(f"{n:<5}{aproximado:<22.15f}{valor_exato:<22.15f}{erro:.15f}")