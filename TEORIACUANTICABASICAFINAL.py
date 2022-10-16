
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
#print(media([[1, -1j], [1j, 2]], [math.sqrt(2)/2, (math.sqrt(2)/2*1j) ]))
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
#print(varianza([[1, -1j], [1j, 2]], [math.sqrt(2)/2, (math.sqrt(2)/2*1j) ]))
def valorpropio(matrix):
    eigenvalues, featurevector = np.linalg.eig(matrix)
    return eigenvalues
def vectorpropio(matrix):
    eigenvalues, featurevector = np.linalg.eig(matrix)
    return featurevector
#Ejercicio 4.3.1
#Elementos comunes:
spinup = np.array([1,0])
observable = np.array([[0,1/2],[1/2,0]])
def ejercicio431(observable):
    vectoresPropios = vectorpropio(observable)
    return vectoresPropios

#print(ejercicio431(observable))
def ejercicio432(observable):
    valoresPropios = valorpropio(observable)
    vectoresPropios = vectorpropio(observable) #Con numpy ya estan normalizados
    accionObservableVector = matxvect(observable, spinup)
    p1 = np.linalg.norm(innerprod(accionObservableVector, vectoresPropios[0]))
    p2 = np.linalg.norm(innerprod(accionObservableVector, vectoresPropios[1]))
    res = p1*valoresPropios[0] + p2*valoresPropios[1]
    return p1, p2, res
#print(ejercicio432(observable))

def ejercicio441(matriz1, matriz2):
    identity  = np.identity(len(matriz1))
    checkunit1 = matriz1 * matriz1.conjugate()
    checkunit2 = np.round(matriz2 * matriz2.conjugate())
    if np.array_equal(checkunit1, identity) and np.array_equal(checkunit2, identity):
        matrizProducto = matriz1 * matriz2
        matrizProductoconjugada = matrizProducto.transpose()
        matrizProductofinal = np.round(matrizProducto * matrizProductoconjugada)
        identity2 = np.identity(len(matrizProducto))
        if np.array_equal(matrizProductofinal, identity2):
            return matrizProducto, True
    return False, False
#Elementos ejercicio
u_1 = np.matrix([[0,1], [1,0]])
u_2 = np.matrix([[math.sqrt(2)/2, math.sqrt(2)/2 ], [math.sqrt(2)/2, -math.sqrt(2)/2]])
matprod, res = ejercicio441(u_1,u_2)
#print("Mat1 ", "\n",  u_1,"\n", "Mat2 ", "\n", u_2,"\n","y su producto", "\n", matprod, "\n", "son unitarias") if res == True else print(False)
def ejercicio442(matriz, estado):
    matriz = np.array(matriz)
    matriz3 = matriz**3
    matrizEstado = matxvect(matriz3,estado)
    res = ProbablidadPos(matrizEstado, 3)
    return res
#Elementos ejercicio
#matriz =[[0, 1/math.sqrt(2),1/math.sqrt(2),0],[1j/math.sqrt(2),0,0,1/math.sqrt(2)],[1/math.sqrt(2),0,0,1j/math.sqrt(2)],[0, 1/math.sqrt(2),-1/math.sqrt(2),0]]
#estado = [1,0,0,0]

#print(ejercicio442(matriz,estado))