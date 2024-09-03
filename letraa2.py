string = input("DIGITE O A: ")

count_a = 0
count_A = 0

for letra in string:
    if letra == 'a':
        count_a += 1
    elif letra == 'A':
        count_A += 1

total = count_a + count_A

if total > 0:
    print("A letra 'a' minúscula apareceu", count_a, "vezes.")
    print("A letra 'A' maiúscula apareceu", count_A, "vezes.")
    print("No total, a letra 'a' apareceu", total, "vezes.")
else:
    print("A letra 'a' não apareceu na string.")
