import matplotlib.pyplot as plt
import numpy
from numpy import *    

## ===================================================================
## PARTE II: PCA
## ===================================================================
def pca(labels, data, classes):
    datalen = len(data)
    
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

    #Y finalmente graficamos:
    plt.plot(e1[0], 'ro',e1[1], 'go',e1[2], 'bo')
    plt.show()
      
    plt.plot(e1[0], e2[0], 'ro',e1[1], e2[1], 'go',e1[2], e2[2], 'bo')
    plt.show()
  
    print E1
