nombresdefamilia = ['Maria', 'Lorena', 'Josefa', 'Antonio', 'David' ];
temperaturasdeJulio = [15, 15, 12, 9, 5, 2, 4, 6, 9, 11, 14, 10, 19, 18, 15, 11, 9, 6, 4, 9, 12, 11, 15, 20, 23, 20, 19, 17, 12, 12, 10];
ciudadesvisitadas= ['Trujillo', 'Caracas', 'Brasilia', 'Cordoba', 'Seul', 'Lousiana'];
eventosimportantes = [1987, 'cumpleaños', 2019];

#ORDENANDO ALFABETICAMENTE
nombresdefamilia.sort()
print(nombresdefamilia);

#ORDEDANDO ASCENDENTEMENTE
temperaturasdeJulio.sort()
print(temperaturasdeJulio);

#Agregando las temperaturas de los 15 dias del mes siguiente
temperaturasdeJulio.append([27, 30, 25, 28, 32, 33, 33, 33, 30, 24, 22, 25, 20, 19, 25])

#Quitando de mi list nombresdefamilia dos elementos 
nombresdefamilia.remove = ('Maria', 'Antonio')
print (nombresdefamilia)