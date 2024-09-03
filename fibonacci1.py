num = int(input("Digite um número: "))

a = 0
b = 1

while a < num:
    c = a + b
    a = b
    b = c

if a == num or num == 0:
    print("o numero pertence a sequência de Fibonacci.")
else:
    print("o numero não pertence a sequência de Fibonacci.")
