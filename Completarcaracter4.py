a = [1, 3, 5, 7]
a.append(a[-1] + 2)
print(a)
#a sequência é 1, 3, 5, 7, e parece que a cada passo estamos somando 2. Então, se a gente seguir a mesma lógica, o próximo número vai ser 7 + 2, que é 9.


b = [2, 4, 8, 16, 32, 64]
b.append(b[-1] * 2)
print(b)

#aqui temos 2, 4, 8, 16, 32, 64, e a cada número está dobrando o anterior. Então, se a gente continuar dobrando, o próximo número vai ser 64 x 2, que dá 128.

c = [0, 1, 4, 9, 16, 25, 36]
c.append((len(c))**2)
print(c)

#olhando para a sequência 0, 1, 4, 9, 16, 25, 36, parece que cada número é o quadrado de um número inteiro: 0², 1², 2², 3², e assim por diante. Então, o próximo número é o quadrado de 7, que é 49.

d = [4, 16, 36, 64]
d.append((len(d) + 2)**2)
print(d)

#a sequência é 4, 16, 36, 64, e parece que cada número é um quadrado de um número par: 2², 4², 6², 8². Então, o próximo número seria 10², que é 100.


e = [1, 1, 2, 3, 5, 8]
e.append(e[-1] + e[-2])
print(e)

#aqui temos 1, 1, 2, 3, 5, 8, que é a famosa sequência de Fibonacci, onde cada número é a soma dos dois anteriores. Então, o próximo número é 5 + 8, que é 13.

f = [2, 10, 12, 16, 17, 18, 19]
f.append(f[-1] + 1)
print(f)

#a sequência é 2, 10, 12, 16, 17, 18, 19, e parece que depois do 19, só estamos adicionando 1. Então, o próximo número vai ser 19 + 1, que é 20.
