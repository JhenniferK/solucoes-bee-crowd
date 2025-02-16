amigos = list(map(str, input().split()))
novosAmigos = list(map(str, input().split()))
indicacao = str(input())
novaLista = []

for i in range(len(amigos)):
    if indicacao == "nao":
        novaLista = amigos
        for k in range(len(novosAmigos)):
            novaLista.append(novosAmigos[k])
        break
    elif amigos[i] == indicacao:
        for j in range(len(novosAmigos)):
            novaLista.append(novosAmigos[j])
    novaLista.append(amigos[i])

print(*novaLista)