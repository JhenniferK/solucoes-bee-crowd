import sys

input = sys.stdin.read
data = input().splitlines()

i = 0
resultados = []

while i < len(data):
    try:
        n = int(data[i])
        custo = int(data[i + 1])
        receitas = [int(data[i + 2 + j]) for j in range(n)]
        i += 2 + n
    except:
        break

    maxLucro = 0
    lucroAtual = 0

    for j in range(n):
        lucroDoDia = receitas[j] - custo

        lucroAtual = max(lucroDoDia, lucroAtual + lucroDoDia)

        maxLucro = max(maxLucro, lucroAtual)

    resultados.append(str(maxLucro))

print("\n".join(resultados))
