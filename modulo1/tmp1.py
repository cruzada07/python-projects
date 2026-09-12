def es_par(a):
    if a%2 == 0:
        return True
    else:
        return False

def es_par_g(a):
    return a%2 == 0

x = 18
print(f"¿El numero {x} es par?: {es_par_g(x)}")
