# -- 1. Fibonacci

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    
    val_calculados = [-1] * (n + 1)
    val_calculados[0], val_calculados[1] = 0, 1

    for i in range(2, n + 1):
        val_calculados[i] = val_calculados[i - 1] + val_calculados[i - 2]

    return val_calculados[n]
        

print(fibonacci(3))



# -- 2. String

def contar_a(texto: str):
    texto_min = texto.lower()
    
    cont = texto_min.count('a')
    
    if cont > 0:
        print(f"A letra 'a' apareceu {cont} vez(es) :)")
    else:
        print("A letra 'a' não apareceu no texto :o")
        

texto= input("Texto: ")
contar_a(texto)


# -- 3. Soma

# Após a ultima iteração, o valor final vai ser 77.

def soma():
    indice = 12
    soma = 0
    k = 1

    while k < indice:
        k += 1
        soma += k

    return soma

print(soma())


# -- 4. Lógica

# a) 9
# b) 128
# c) 50
# d) 102
# e) 13
# f) 20

# -- 5. Lampadas

# É preciso levar em consideração se a lampada está quente ou não:

# ligar interruptor 1 por um certo tempo e desligar em seguida. 
# deixar o 2 ligado e manter o 3 desligado.

# Se na sala ao entrar uma das lampads estiver: 
# quente -> o inter. 1 a acende; 
# ligada -> o inter. 2 a acende;
# desligada -> o inter. 3 a acende;
