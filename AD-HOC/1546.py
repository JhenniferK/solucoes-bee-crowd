qtdCasos = int(input())

dic = { 1:"Rolien",
        2:"Naej",
        3:"Elehcim",
        4:"Odranoel"
}

for i in range(qtdCasos):
    qtdFeed = int(input())
    for j in range(qtdFeed):
        chave = int(input())
        print(dic[chave])