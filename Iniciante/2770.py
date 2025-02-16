import sys

input = sys.stdin.read
dados = input().splitlines()

i = 0
while i < len(dados):
    try:
        X, Y, M = map(int, dados[i].split())
        i += 1
        for _ in range(M):
            Xi, Yi = map(int, dados[i].split())
            i += 1
            if (Xi <= X and Yi <= Y) or (Yi <= X and Xi <= Y):
                print("Sim")
            else:
                print("Nao")
    except:
        break
