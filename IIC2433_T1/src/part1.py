import matplotlib.pyplot as plt
import numpy
from numpy import *    

# Imprimimos diferentes combinaciones de 2 componentes
def plotData2d(labels, data, classes):
    #3. Imprimimos las difentes combinaciones
    datalen = len(data)
    
    # Arreglo que separa las variables en distintas columnas:
    x = [[data[i][j] for i in range(len(data))] for j in range(4)]
    
    # Arreglos auxiliares, cada uno contiene la variable 'xi' agrupada por la clase a la que pertenece:
    x0 = [[x[0][i] for i in range(datalen) if labels[i] == classes[j]] for j in range(len(classes))]
    x1 = [[x[1][i] for i in range(datalen) if labels[i] == classes[j]] for j in range(len(classes))]
    x2 = [[x[2][i] for i in range(datalen) if labels[i] == classes[j]] for j in range(len(classes))]
    x3 = [[x[3][i] for i in range(datalen) if labels[i] == classes[j]] for j in range(len(classes))]
    
    #x_per_class = [[[x[k][i] for i in range(datalen) if labels[i] == classes[j]] for j in range(len(classes))] for k in len(x)]
    #print len(x_per_class)
    
    plt.plot(x0[0], x1[0], 'ro',x0[1], x1[1], 'go',x0[2], x1[2], 'bo')
    plt.show()

    plt.plot(x0[0], x2[0], 'ro',x0[1], x2[1], 'go',x0[2], x2[2], 'bo')
    plt.show()

    plt.plot(x0[0], x3[0], 'ro',x0[1], x3[1], 'go',x0[2], x3[2], 'bo')
    plt.show()

    plt.plot(x1[0], x2[0], 'ro',x1[1], x2[1], 'go',x1[2], x2[2], 'bo')
    plt.show()

    plt.plot(x1[0], x3[0], 'ro',x1[1], x3[1], 'go',x1[2], x3[2], 'bo')
    plt.show()

    plt.plot(x2[0], x3[0], 'ro',x2[1], x3[1], 'go',x2[2], x3[2], 'bo')
    plt.show()

