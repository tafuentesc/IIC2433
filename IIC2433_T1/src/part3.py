import matplotlib.pyplot as plt
import numpy
from numpy import *    

## ===================================================================
## PARTE III: Fisher
## ===================================================================
def fisher(labels, data, classes):    
    datalen = len(data)
    
    # Primero, separamos la informacion en 2 clases
    for j in range(len(classes)):
        data2 = [[data[i] for i in range(datalen) if labels[i]==classes[j]],[data[i] for i in range(datalen) if labels[i]!=classes[j]]]
        
        # Extraemos las medias para los 2 sets de datos:
        array2 = [numpy.array(data2[0]), numpy.array(data2[1])]
        means2 = [array2[0].mean(0), array2[1].mean(0)]
    
        print means2
        
        # Normalizamos los datos (restamos las medias):
        B1 = data2[0] - means2[0]
        B2 = data2[1] - means2[1]
    
        # Hecho esto, procedemos a calcular las sparse matrices:
        S1 = dot(B1.transpose(), B1)
        S2 = dot(B2.transpose(), B2)
        
        # Calculamos Sw, que mide varianza dentro de las clases:
        Sw = S1 + S2
        
        # Finalmente, resolvemos para obtener la direccion de maxima separacion, V:
        Sw_inv = linalg.inv(Sw)
        
        V = dot(Sw_inv, (means2[0] - means2[1]))
        
        # Obtenido V, procedemos a proyectar los datos y graficar:
        
        fisher1 = dot(V.transpose(), array2[0].transpose())    
        fisher2 = dot(V.transpose(), array2[1].transpose())    
        
        plt.plot(fisher1, 'ro', fisher2, 'bo')
        plt.show()