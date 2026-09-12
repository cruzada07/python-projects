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

# 3. Dict

persona = {
    "nombre" : "Carlos",
    "edad" : 25,
    "ciudad" : "Lima"
}
#   No usamos indices, usamos claves
print(persona["ciudad"])
persona["nombre"] = "Miguel"        # SI PODEMOS modificarlo
persona["profesion"] = "Programador"# Tambien podemos agregar informacion

#   ¿Cuando usar Dict?
#       Cuando quieres representar informacion mediante caracteristicas(claves)
#   -> Dict = clave -> valor

#   --------------------------------------------------------------------

# 4. Set

numbers = {1,2,3}   # NO permite elementos repetidos
names = {"Maria", "Marcelo", "Marisol", "Kevin", "Maria", "Marisol", "Raul"}
unicos = set(names)
print(names)
print(unicos)   # Es lo mismo

a = {1,2,3}
b = {3,4,5}
print(a | b)    # Union
print(a & b)    # Interseccion
print(a - b)    # Diferencia

#   ¿Cuando usar Set?
#       Cuando vas a agrupar informacion y quieres evitar elementos repetidos
#   -> Set = Colección de elementos únicos
