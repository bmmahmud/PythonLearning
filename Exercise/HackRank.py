# Animal
lists = ["vertebrado","ave","onivoro"]
# for x in range(3):
#     aa = input()
#     lists.append(aa)  
if lists[0] == 'vertebrado':
    if lists[1] == 'mamifero':
        if lists[2] == 'onivoro':
            print('homem')
        elif lists[2] == 'herbivoro':
            print('vaca')
    elif lists[1] == 'ave':
        if lists[2] == 'carnivoro':
            print('aguia')
        if lists[2] == 'onivoro':
            print('pomba')
elif lists[0] == 'invertebrado':
    if lists[1] == 'inseto':
        if lists[2] == 'hematofago':
            print('pulga')
        elif lists[2] == 'herbivoro':
            print('lagarta')
    elif lists[1] == 'anelideo':
        if lists[2] == 'hematofago':
            print('sanguessuga')
        elif lists[2] == 'onivoro':
            print('minhoca')            
