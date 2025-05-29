#Operaciones con DNIs
#Ingreso de los DNIs
Abril= "42128028"
Yamila= "39603954"
Natalia= "42768065"
Carolina ="39327728"
Daiana="38722101"

# Generación automática de los conjuntos de dígitos únicos.
A= set(Abril)
Y= set(Yamila)
N= set(Natalia)
C= set(Carolina)
D= set(Daiana)

#funcion operaciones de conjuntos con posibilidad de elegir la operacion y agregar una cantidad de conjuntos variables 
def operaciones(operacion,conjunto1, conjunto2, *conjuntos):
    metodo_a_ejecutar = getattr(conjunto1, operacion)
    operacion_conjunto = metodo_a_ejecutar(conjunto2)
    if conjuntos:
        for conjunto in conjuntos:
            metodo_a_ejecutar_siguiente = getattr(operacion_conjunto, operacion)
            operacion_conjunto = metodo_a_ejecutar_siguiente(conjunto)
    return operacion_conjunto

#visualización de: unión, intersección, diferencias y diferencia simétrica.
print("Tenemos 5 DNIs, con los que vamos a generar conjuntos de dígitos unicos")
print(f"DNI de Abril es {Abril} su conjunto es {A}")
print(f"DNI de Yamila es {Yamila} su conjunto es {Y}")
print(f"DNI de Natalia es {Natalia} su conjunto es {N}")
print(f"DNI de Carolina es {Carolina} su conjunto es {C}")
print(f"DNI de Daiana es {Daiana} su conjunto es {D}")

print("como ejemplo realizaremos la union de todos los conjuntos dando como resultado=",operaciones("union",A,N,D,Y,C))
print("otros ejemplos de union")
print("A ∪ N ∪ C = ",operaciones("union",A,N,C))
print("Y ∪ D =", operaciones("union",Y,D))

print("ejemplos de interseccion")
print("Y ∩ C =",operaciones("intersection",Y,C))
print("C ∩ N =",operaciones("intersection",C,N))
print("A ∩ D =",operaciones("intersection",A,D))
print("Y ∩ A ∩ N =",operaciones("intersection",Y,A,N))

print("ejemplo de diferencia")
print("Y - C =",operaciones("difference",Y,C))
print("Y - N =",operaciones("difference",Y,N))
print("A - C =",operaciones("difference",A,C))
print("D - A =",operaciones("difference",D,A))

print("ejemplo de diferencia simetrica")
print("A Δ C =",operaciones("symmetric_difference",A,C))
print("D Δ N =",operaciones("symmetric_difference",D,N))
print("C Δ Y =",operaciones("symmetric_difference",C,Y))
print("D Δ A =",operaciones("symmetric_difference",D,A))

#Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
def conteo_digitos(dni):
    for i in range (0,10):
        contador =0
        for digito in dni:
            if i == int(digito):
                contador +=1
        print(f"{i} se repite {contador} veces")

print(f"Repeticion de digitos del DNI {Carolina}")
conteo_digitos(Carolina)

#Suma total de los dígitos de cada DNI.
def suma_digitos(dni):
    suma =0
    for digito in dni:
        suma = int(digito) + suma
    print(f"la suma del DNI {dni} es {suma}")

print("suma de los digitos del DNI")
suma_digitos(Abril)
suma_digitos(Yamila)
suma_digitos(Natalia)
suma_digitos(Carolina)
suma_digitos(Daiana)
#Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.
# Ejemplos:
#Si un dígito aparece en todos los conjuntos, mostrar "Dígito compartido".
#Si algún conjunto tiene más de 6 elementos, mostrar "Diversidad numérica alta".

#B. Operaciones con años de nacimiento
#Ingreso de los años de nacimiento de las 5 integrantes.
año_nacimiento = []
print("Ingrese los años de nacimiento de los 5 integrantes:")
for i in range(5):
    while True:
        año = int(input(f"Integrante {i+1}: "))
        año_nacimiento.append(año)
        break


#Contar nacidas en años pares e impares.
pares = 0
impares = 0
for año in año_nacimiento:
    if año % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Integrantes nacidas en años pares: {pares}")
print(f"Integrantes nacidas en años impares: {impares}")


#Clasificar los años segun su generación.
generacion_x = 0
generacion_y = 0
generacion_z = 0
generacion_alpha = 0

print("\nClasificación de los años segun su generacion:")
for año in año_nacimiento:
    if 1960 <= año <= 1979:
        if generacion_x == 0:
            print("Años correspondientes a la generación X:", end=" ")
        generacion_x += 1
        print(año, end=" ")
    elif 1980 <= año <= 1994:
        if generacion_y == 0:
            print("\nAños correspondientes a la generación Y:", end=" ")
        generacion_y += 1
        print(año, end=" ")
    elif 1995 <= año <= 2009:
        if generacion_z == 0:
            print("\nAños correspondientes a la generación Z:", end=" ")
        generacion_z += 1
        print(año, end=" ")
    elif año >= 2010:
        if generacion_alpha == 0:
            print("\nAños correspondientes a la generación Alpha:", end=" ")
        generacion_alpha += 1
        print(año, end=" ")

#Determinar si un año es bisiesto
def bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False
    
# Verificar si alguno nació en año bisiesto y mostrar cuáles
año_bisiesto = [año for año in año_nacimiento if bisiesto(año)]

if año_bisiesto:
    print("\n¡Tenemos años especiales!")
    print("Los años bisiestos de esta lista son: ", ", ".join(map(str, año_bisiesto))) 
    #Toma la lista de años bisiestos, convierte cada número a una cadena de texto 
    # y une todas esas cadenas en una sola, separando los años con una coma y un espacio.
else:
    print("\nNinguno nació en un año bisiesto.")

# Calcular el producto cartesiano entre años y edades

#Calcular edad actual
def calcular_edad(año_nacimiento):
    año_actual = 2025
    return año_actual - año_nacimiento
edades = [calcular_edad(año) for año in año_nacimiento]

producto_cartesiano = []
for año in año_nacimiento:
    for edad in edades:
        producto_cartesiano.append((año, edad))

print("El producto cartesiano entre el año de nacimiento y la edad actual es: ")
for par in producto_cartesiano:
    print(par)
