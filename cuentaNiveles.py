listaNiveles = []
mario = 0
up = 0
same = 0
down = 0
print('ingresa la lista de los niveles. Escriba "basta" para terminar')
while True:
    valor = input('Ingresa el nivel: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            listaNiveles.append(valor)
        except:
            print('no se puede compa')
            exit()
mario = listaNiveles[0]
for x in listaNiveles:
    if mario > x:
        down += 1
        mario = x
    elif mario < x:
        up += 1
        mario = x
    elif mario == x:
        same += 1
        mario = x 


print('arriba: ', up)
print('abajo: ', down)
print('mismo nivel: ', same - 1)