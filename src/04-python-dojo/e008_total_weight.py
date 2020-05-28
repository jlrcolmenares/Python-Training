
productos = input('Introduce descripción de productos (lista): ')
productos = ['tazas','bolsas de café']
pesos = [34, 45]
cantidades = [10,3]
for i in range(len(pesos)):
    pesos_totales.append(pesos[i]*cantidades[i])
print('{} {} y {} {} pesan {}'.format(cantidades[0],productos[0],cantidades[1],productos[1], sum(pesos_totales)))
