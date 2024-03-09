"""3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____"""

#3-a)
n1 = 1
n2 = 3
sequencia = []
count = n2 - n1
while count < 6:
    sequencia.append(n1 + (count * 2))
    count += 1
print(sequencia)

#3-b)
n1 = 2
n2 = 4
sequencia2 = []
mult = n2 - n1
for i in range(7):
    sequencia2.append(n1 * mult ** i)
print(sequencia2)

#3-c)
base = 1
exp = 2
sequencia3 = [base]
while len(sequencia3) <  7:
    sequencia3.append((base + 1) ** exp)
    base += 1
print(sequencia3)

#3-d)
seq = [4, 16, 36, 64]
razões = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
razao = razões[-1] + 8

proxNum = seq[-1] + razao
seq.append(proxNum)

print(seq)

#3-e)
def fibo(n):
    seq = [1, 1]
    while seq[-1] < n:
        seq.append(seq[-1]+seq[-2])
    return seq

num = 9
print(fibo(num))

#3-f)
#o proximo valor seria duzentos pois todos os numero começam com a letra 'd' logo, o proximo numero sera 200
