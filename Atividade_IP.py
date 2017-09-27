linhas = readlines()
ind1 = 1
ind2 = 2
ind3 = 3
ind4 = 4

for x in range (0,len(linhas)):
    a = linha.split(".")
    ponto = []
    ponto.append(a)
    for l in range(0,len(ponto)):

        if ponto [ind1] > 0 and ponto[ind1] <= 255 and ponto[ind2] > 0 and ponto[ind2] <= 255 and ponto [ind3] > 0 and ponto[ind3] <= 255 and ponto [ind4] > 0 and ponto[ind4] <= 255:
            print("Endereço de IP (1).(2).(3).(4) É válido".format(ind1, ind2, ind3, ind4))
            ind1 = ind1 + 4
            ind2 = ind2 + 4
            ind3 = ind3 + 4
            ind4 = ind4 + 4

        else:
            print("Endereço de IP (1).(2).(3).(4) É inválido".format(ind1, ind2, ind3, ind4))
    
