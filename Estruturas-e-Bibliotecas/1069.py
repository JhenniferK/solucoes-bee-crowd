def contar_diamantes(sequencia):
    pilha = []
    diamantes = 0
    
    for caractere in sequencia:
        if caractere == '<':
            pilha.append(caractere)
        elif caractere == '>' and pilha:
            pilha.pop()
            diamantes += 1
    
    return diamantes

N = int(input())

for _ in range(N):
    sequencia = input().strip()
    print(contar_diamantes(sequencia))