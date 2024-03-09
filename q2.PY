"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência."""

def fibo(n):
    seq = [0, 1]
    while seq[-1] < n:
        seq.append(seq[-1]+seq[-2])
    return seq

def checkFibo(n):
    seq = fibo(n)
    if n in seq:
        return f'O número {n} Faz parte da sequencia de Fibonacci'
    else:
        return f'O número {n} Não faz parte da sequencia de Fibonacci'

num = int(input('Informe um número para verificar a sequencia de Fibonacci: '))
print(fibo(num))
print(checkFibo(num))
