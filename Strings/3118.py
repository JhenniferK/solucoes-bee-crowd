from collections import defaultdict

n, m = map(int, input().split())
regras = {}

for _ in range(m):
    grupo, resultado = input().split()
    regras[grupo] = resultado

linha_atual = 'A'

for _ in range(n):
    grupos = []
    i = 0

    while i < len(linha_atual):
        j = i
        while j < len(linha_atual) and linha_atual[j] == linha_atual[i]:
            j += 1
        grupos.append(linha_atual[i:j])
        i = j

    next_line = []
    for grupo in grupos:
        if grupo in regras:
            next_line.append(regras[grupo])

    linha_atual = ''.join(next_line)

a_count = linha_atual.count('A')
b_count = linha_atual.count('B')

print(a_count, b_count)
