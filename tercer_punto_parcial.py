from collections import deque

# Definir la clase Misión
class Misión:
    def __init__(self, planeta, capturado, recompensa):
        self.planeta = planeta
        self.capturado = capturado
        self.recompensa = recompensa

# Crear una pila para almacenar las misiones
bitacora = deque()

# Función para mostrar los planetas visitados en el orden de las misiones
def mostrar_planetas_visitados():
    planetas_visitados = [mision.planeta for mision in bitacora]
    print("Planetas visitados en el orden de las misiones:")
    for planeta in planetas_visitados:
        print(planeta)

# Función para determinar la suma total de los créditos galácticos recaudados
def calcular_creditos_galacticos():
    total_creditos = sum(mision.recompensa for mision in bitacora)
    return total_creditos

# Función para determinar el número de la misión en la que capturó a Han Solo y el planeta correspondiente
def buscar_mision_han_solo():
    for i, mision in enumerate(bitacora, start=1):
        if mision.capturado == "Han Solo":
            return i, mision.planeta

# Ejemplo de llenado de la bitácora con algunas misiones
bitacora.append(Misión("Tatooine", "Jabba the Hutt", 500))
bitacora.append(Misión("Bespin", "Lando Calrissian", 1000))
bitacora.append(Misión("Endor", "Ewoks", 800))
bitacora.append(Misión("Hoth", "Han Solo", 2000))  # Suponemos que capturó a Han Solo en esta misión

# a. Mostrar los planetas visitados en el orden de las misiones
mostrar_planetas_visitados()

# b. Determinar cuántos créditos galácticos recaudó en total
total_creditos = calcular_creditos_galacticos()
print("Créditos galácticos recaudados en total:", total_creditos)

# c. Determinar el número de la misión en la que capturó a Han Solo y en qué planeta fue
numero_mision_han_solo, planeta_mision_han_solo = buscar_mision_han_solo()
print("Número de la misión en la que capturó a Han Solo:", numero_mision_han_solo)
print("Planeta en el que capturó a Han Solo:", planeta_mision_han_solo)