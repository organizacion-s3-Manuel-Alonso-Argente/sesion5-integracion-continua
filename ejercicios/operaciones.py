# En principio el alumno solo recibiría la definición de la función en el archivo correspondiente
def suma(x,y):

    # El alumno deberá implementar correctamente el código de la función para pasar el test correspondiente
    return x + y

#Función para saber si un número es par o impar
def es_par(x):
    #Si el resto de la división da 0 es porque el número es par.
    if x%2 == 0:
        return "par"
    else:
        return "impar"
