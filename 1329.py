while(True):
    partidas = int(input())
    if partidas == 0:
        break
    res = input()
    res = res.split()
    mary = 0
    john = 0
    for i in range(len(res)):
        
        if int(res[i]) == 0 :
            mary += 1
        else:
            if int(res[i]) == 1:
                john += 1
    print('Mary won {} times and John won {} times'.format(mary, john))