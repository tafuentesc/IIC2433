import matplotlib.pyplot as plt
import numpy
from numpy import *    

def part1():
    #1. Abrimos el archivo y cargamos los datos
    iris_file = open('../data/iris.data.txt', 'r')
    iris_data = iris_file.readlines() 
    iris_file.close()
    
    classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
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
    
    print data
    print labels
    
    #Seteamos colores
    colors = []
    
    for label in labels:
        if label == classes[0]:
            colors.append('r')
        elif label == classes[1]:
            colors.append('g')
        elif label == classes[2]:
            colors.append('b')
    
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
    
    #-------- plt.plot(x0[0], x1[0], 'ro',x0[1], x1[1], 'go',x0[2], x1[2], 'bo')
    #---------------------------------------------------------------- plt.show()
#------------------------------------------------------------------------------ 
    #-------- plt.plot(x0[0], x2[0], 'ro',x0[1], x2[1], 'go',x0[2], x2[2], 'bo')
    #---------------------------------------------------------------- plt.show()
#------------------------------------------------------------------------------ 
    #-------- plt.plot(x0[0], x3[0], 'ro',x0[1], x3[1], 'go',x0[2], x3[2], 'bo')
    #---------------------------------------------------------------- plt.show()
#------------------------------------------------------------------------------ 
    #-------- plt.plot(x1[0], x2[0], 'ro',x1[1], x2[1], 'go',x1[2], x2[2], 'bo')
    #---------------------------------------------------------------- plt.show()
#------------------------------------------------------------------------------ 
    #-------- plt.plot(x1[0], x3[0], 'ro',x1[1], x3[1], 'go',x1[2], x3[2], 'bo')
    #---------------------------------------------------------------- plt.show()
#------------------------------------------------------------------------------ 
    #-------- plt.plot(x2[0], x3[0], 'ro',x2[1], x3[1], 'go',x2[2], x3[2], 'bo')
    #---------------------------------------------------------------- plt.show()

    ## ===================================================================
    ## PARTE II: PCA
    ## ===================================================================
    
    # Hacemos arreglo auxiliar que usaremos para calcular las medias:
    array = numpy.array(data)
    means = array.mean(0)
    
    # Normalizamos los datos (restamos las medias):
    B = data - means

    # Hecho esto, procedemos a calcular la matriz de covarianza:
    COV = dot(B.transpose(), B) / (datalen - 1)
    
    # Posteriormente, sacamos las componentes principales:
    [values, vectors] = linalg.eig(COV)
    
    # Las ordenamos de mayor a menor:
    sort_index = numpy.argsort(values)
    sort_index = sort_index[::-1]
    
    sort_values = [values[sort_index[i]] for i in range(len(sort_index))]
    sort_vectors = [vectors[sort_index[i]] for i in range(len(sort_index))]

    print sort_vectors[0]
    #print len(data) +","+
    
    # Y proyectamos en las 2 direcciones principales
    E1 = dot(sort_vectors[0].transpose(), array.transpose())    
    #E1_proy = [E1[i] * sort_vectors[0] for i in E1]
    E2 = dot(sort_vectors[1].transpose(), array.transpose())    

    # Separamos por clases...
    e1 = [[E1[i] for i in range(len(E1)) if labels[i] == classes[j]] for j in range(len(classes))]
    e2 = [[E2[i] for i in range(len(E1)) if labels[i] == classes[j]] for j in range(len(classes))]

    # Y finalmente graficamos:
    plt.plot(e1[0], 'ro',e1[1], 'go',e1[2], 'bo')
    plt.show()
    
    plt.plot(e1[0], e2[0], 'ro',e1[1], e2[1], 'go',e1[2], e2[2], 'bo')
    plt.show()

    print E1