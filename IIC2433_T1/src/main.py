import sys
from part1 import *
from part2 import *
from part3 import *

# Variables globales que usaremos en el programa
classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
data = []
labels = []

def main(argv=None):
    # Cargamos los datos
    [labels, data] = read_file() 
    
    # Mostramos el menu:
    running = True
    
    while(running):
        print 'Bienvenido a IIC2433 - Tarea 1'
        print '1) Imprimir graficos 2D'
        print '2) Calcular PCA'
        print '3) Calcular Fisher'
        print '4) Salir'
        
        option = raw_input('Seleccione opcion: ')
        
        if(option == '1'):
            # PARTE 1: imprimimos los graficos
            plotData2d(labels, data, classes)
            
        elif(option == '2'):
            pca(labels, data, classes)
        
        elif(option == '3'):
            fisher(labels, data, classes)

        elif(option == '4'):
            running = False

    print 'Programa terminado exitosamente'
    
# Reads the data stored in file. Returns [labels, data].
def read_file(file='../data/iris.data.txt'):

    #1. Abrimos el archivo y cargamos los datos
    iris_file = open(file, 'r')
    iris_data = iris_file.readlines() 
    iris_file.close()
    
    data = []
    labels = []
    
    #2. separamos el contenido de las lineas:
    for entry in iris_data:
        entry = entry.rstrip()
        array = entry.split(',')
        
        if len(array) > 1:
            labels.append(array[4])
    
            array = [float(i) for i in array[0:4]]
            data.append(array)         

    #3. Retornamos informacion
    return [labels, data]

if  __name__ =='__main__':
    main()
