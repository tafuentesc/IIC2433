import sys
import numpy
from part1 import *
from part2 import *
from part3 import *

def main(argv=None):
    # Definimos clases a usar:
    classes = [2,3,4,5,6,7,8,9]
    
    # Cargamos los datos
    [labels, data, column_names] = read_file() 
    
    # Mostramos el menu:
    running = True
    
    while(running):
        print 'Bienvenido a IIC2433 - Tarea 2'
        print '1) Imprimir scores KNN'
        print '2) Imprimir scores Decision Tree'
        print '3) Imprimir scores Naive Nayes'
        print '4) Salir'
        
        option = raw_input('Seleccione opcion: ')
        
        if(option=='1'):
            KNN_classifier(data, labels, 5)
            KNN_classifier(data, labels, 8)
            KNN_classifier(data, labels, 15)
            
        elif(option == '2'):
            DT_classifier(data, labels)
       
        elif(option == '3'):
            GaussianNB_classifier(data, labels)

        elif(option == '4'):
            running = False
        
#===============================================================================
#         if(option == '1'):
#             # PARTE 1: imprimimos los graficos
#             plotData2d(labels, data, classes)
#             
#         elif(option == '2'):
#             pca(labels, data, classes)
#         
#         elif(option == '3'):
#             fisher(labels, data, classes)
# 
#         elif(option == '4'):
#             running = False
#===============================================================================

    print 'Programa terminado exitosamente'
    
# Reads the data stored in file. Returns [labels, data].
def read_file(file='../data/data.txt'):

    #1. Abrimos el archivo:
    fileStream = open(file, 'r')
    
    # Cargamos los nombres de las columnas
    aux =  fileStream.readline()
    aux = aux.rstrip('#')
    aux = aux.rstrip('\n')
    column_names = aux.split(' ')
    
    # Cargamos el resto de los datos
    data = numpy.loadtxt(fileStream, usecols=range(1, len(column_names)))
    
    # Extraemos los labels de data
    labels = data[:, -1]
    data = data[:, 0:len(data[1][:])-1]
    
    #3. Retornamos informacion
    return [labels, data, column_names]

if  __name__ =='__main__':
    main()
