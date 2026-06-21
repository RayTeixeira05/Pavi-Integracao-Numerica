#Cálculo de integrais definidas pelo Teorema Fundamental do Cálculo

#Todas as Modificação em relação ao pseudocódigo foram descritas abaixo:

#Foi necessário importar funções matemáticas e o valor de π,
#para trabalhar com sen(x), e^x e o intervalo [0, π]
from math import cos, exp, pi


#Em vez de definir apenas uma primitiva, foram definidas três
#Uma para cada função do exercício.

#Primitiva de f(x) = x²
def F1(x):
    return x**3 / 3   #F1(x) = x³/3

#Primitiva de f(x) = sen(x)
def F2(x):
    return -cos(x)    #F2(x) = -cos(x)

#Primitiva de f(x) = e^x
def F3(x):
    return exp(x)     #F3(x) = e^x

#Cálculo da integral de f(x) = x² no intervalo [0,1]
a = 0
b = 1
integral = F1(b) - F1(a) #Aplicação do Teorema Fundamental do Cálculo.

#Exibe o resultado da integral calculada
print("∫[0,1] x² dx =", integral)


#Cálculo da integral de f(x) = sen(x) no intervalo [0,π]
a = 0
b = pi
integral = F2(b) - F2(a)  #Aplicação do Teorema Fundamental do Cálculo.

#Exibe o resultado da integral calculada
print("∫[0,π] sen(x) dx =", integral)


# Cálculo da integral de f(x) = e^x no intervalo [0,1]
a = 0
b = 1
integral = F3(b) - F3(a)  #Aplicação do Teorema Fundamental do Cálculo.

#Exibe o resultado da integral calculada
print("∫[0,1] e^x dx =", integral)