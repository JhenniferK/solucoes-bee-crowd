while True:
    totalPostes = int(input())

    if totalPostes == 0:
        break
    else:
        postes = list(map(int, input().split()))
        seguidos = 0
        total = 0
        
        for i in range(len(postes)):
            if postes[i] == 0:
                seguidos += 1
            else:
                if seguidos % 2 != 0:
                    total += (seguidos - 1) // 2
                else:
                    total += seguidos // 2
                seguidos = 0
        
        if seguidos > 0:
            if seguidos % 2 != 0:
                total += (seguidos - 1) // 2
            else:
                total += seguidos // 2

        if postes[0] == 0 and postes[-1] == 0:
            inicio = 0
            while inicio < len(postes) and postes[inicio] == 0:
                inicio += 1

            fim = len(postes) - 1
            while fim >= 0 and postes[fim] == 0:
                fim -= 1

            zerosInicio = inicio
            zerosFim = len(postes) - 1 - fim

            totalZeros = zerosInicio + zerosFim

            if totalZeros % 2 != 0:
                total += (totalZeros - 1) // 2
            else:
                total += totalZeros // 2

            if zerosInicio % 2 != 0:
                total -= (zerosInicio - 1) // 2
            else:
                total -= zerosInicio // 2

            if zerosFim % 2 != 0:
                total -= (zerosFim - 1) // 2
            else:
                total -= zerosFim // 2

        print(total)