n = int(input())
mapa = []

for _ in range(n + 1):
    linha = list(map(int, input().split()))
    mapa.append(linha)

resultado = []
for i in range(n):
    linha_resultado = ''
    for j in range(n):
        total_cameras = mapa[i][j] + mapa[i][j + 1] + mapa[i + 1][j] + mapa[i + 1][j + 1]
        if total_cameras >= 2:
            linha_resultado += 'S'
        else:
            linha_resultado += 'U'
    resultado.append(linha_resultado)

for linha in resultado:
    print(linha)
