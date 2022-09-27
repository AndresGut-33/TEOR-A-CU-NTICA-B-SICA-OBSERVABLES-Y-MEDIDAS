import math
import numpy as np
def ProbablidadPos(Vect, pos):
    '''
    Nos permite sacarcalcular la probabilidad de encontrarlo en una posición en particular.
    (List 1D, INT) - > Real
    '''
    norma = 0
    for i in Vect:
        norma += abs(i) ** 2
    Elemento = abs(Vect[pos-1]) ** 2
    return Elemento / norma
#print(ProbablidadPos([3 - 4J, 7 + 2J], 1))
def ProbVectVect(vec1, vect2):
    '''
    El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo
    (List 1D, List 1D) - > Real
    '''
    norm_1 = np.linalg.norm(vec1)
    norm_2 = np.linalg.norm(vect2)
    for i in range(len(vec1)):
        vec1[i] = vec1[i] / norm_1
        vect2[i] = vect2[i] / norm_2
    inner_prod = 0
    for i in range(len(vec1)):
        multi = vect2[i] * vec1[i].conjugate()
        inner_prod += multi
    return inner_prod
#print(ProbVectVect([1, -1j], [-1j, 1]))