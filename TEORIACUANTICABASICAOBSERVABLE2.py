import math
import numpy as np
def ProbablidadPos(Vect, pos):
    '''
    Nos permite calcular la probabilidad de encontrarlo en una posición en particular.
    (List 1D, INT) - > Real
    '''
    norma = 0
    for i in Vect:
        norma += abs(i) ** 2
    Elemento = abs(Vect[pos]) ** 2
    return Elemento / norma
#print(ProbablidadPos([2+ 1j, -1 +2j, 1j, 1, 3-1j, 2, -2j, -2+1j, 1-3j, -1j], 9))
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
#print(ProbVectVect([1,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,1,0,0,0]))
def Hermitian(a):
    a = np.array(a)
    a_conjugada = np.conjugate(a)
    return np.array_equal(a, np.transpose(a_conjugada))
#print(Hermitian([[1, 1], [1, -1]]))
def norm_vect(vect):
    norm_vect = np.linalg.norm(vect)
    for i in range(len(vect)):
        vect[i] = vect[i] / norm_vect
    return vect
def matxvect(mat, vect):
    mat = np.array(mat)
    vect = np.array(vect)
    return mat.dot(vect)
def innerprod(vect1, vect2):
    inner_prod = 0
    for i in range(len(vect1)):
        multi = vect2[i] * vect1[i].conjugate()
        inner_prod += multi
    return inner_prod
def media(observable, vect):
    if Hermitian(observable):
        vect = norm_vect(vect)
        vectprod = matxvect(observable, vect)
        media = innerprod(vectprod, vect)
        return media
    return False
print(media([[1, -1j], [1j, 2]], [math.sqrt(2)/2, (math.sqrt(2)/2*1j) ]))
def varianza(observable, vect):
    if media != False:
        media_ = media(observable, vect)
        identity = np.identity(len(vect))
        mediaxidentity = media_ * identity
        resta = np.matrix(observable) - np.matrix(mediaxidentity)
        restacuadrado = np.matrix(resta).dot(np.matrix(resta))
        res = media(restacuadrado, vect)
        return res
    return False
print(varianza([[1, -1j], [1j, 2]], [math.sqrt(2)/2, (math.sqrt(2)/2*1j) ]))

