# estructuras de datos

#   --------------------------------------------------------------------

# 1. List

numeros = [10, 20, 30]

print(numeros[0])   #10
numeros.append(40)  #numeros[3] = 40
numeros[0] = 100    #10 -> 100
print(numeros)

frutas = ["manzana", "pera", "manzana"] #acepta repetidos
print(frutas)

#   ¿Cuando usar List?
#       Cuando tienes una colección de elementos que puede cambiar
#   -> List = Colección ordenada que puede cambiar

#   --------------------------------------------------------------------

# 2. Tuple

nms = (10, 20, 30)

print(nms[2])
#   NO SE PUEDE MODIFICAR -> nms[0] = 100  X
punto = (10,20)
dias = ("lunes", "martes", "miercoles","jueves")

#   ¿Cuando usar Tuple?
#       Cuando tienes un conjunto de datos que NO deberia modificarse
#   -> Tuple = Una lista que NO puedes modificar

#   --------------------------------------------------------------------

