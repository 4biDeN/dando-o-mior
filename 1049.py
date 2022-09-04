classe = input()
subclasse = input()
comida = input()

if classe == 'vertebrado':
    if subclasse == 'ave':
        if comida == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if subclasse == 'mamifero':
            if comida == 'onivoro':
                print('homem')
            else:
                print('vaca')
if classe == 'invertebrado':
    if subclasse == 'inseto':
        if comida == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if subclasse == 'anelideo':
            if comida == 'hematofago':
                print('sanguessuga')
            else:
                print('minhoca')