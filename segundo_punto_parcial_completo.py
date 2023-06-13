from collections import deque

# Definir la lista principal de personajes
avengers = [
    ("Iron Man", "Tony Stark", "", 1963),
    ("Captain America", "Steve Rogers", "", 1941),
    ("Black Widow", "Natasha Romanoff", "", 1964),
    ("Hawkeye", "Clint Barton", "", 1964),
    ("Thor", "", "", 1962),
    ("Hulk", "", "", 1962),
    ("Captain Marvel", "", "", 1967),
    ("Scarlet Witch", "Wanda Maximoff", "", 1964),
    ("Vision", "", "", 1968),
    ("Black Panther", "T'Challa", "", 1966),
    ("Star-Lord", "Peter Quill", "Guardianes de la galaxia", 1976),
    ("Gamora", "", "Guardianes de la galaxia", 1975),
    ("Drax", "", "Guardianes de la galaxia", 1973),
    ("Rocket Raccoon", "", "Guardianes de la galaxia", 2008),
    ("Groot", "", "Guardianes de la galaxia", 2006),
    ("Mr. Fantastic", "Reed Richards", "Los cuatro fantásticos", 1961),
    ("Invisible Woman", "Sue Storm", "Los cuatro fantásticos", 1961),
    ("Human Torch", "Johnny Storm", "Los cuatro fantásticos", 1961),
    ("The Thing", "Ben Grimm", "Los cuatro fantásticos", 1961)
]

# a. Determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje
nombre_superheroe_buscado = "Capitana Marvel"
for personaje in avengers:
    if personaje[0] == nombre_superheroe_buscado:
        nombre_personaje = personaje[1]
        print("El nombre de personaje de", nombre_superheroe_buscado, "es:", nombre_personaje)
        break
else:
    print(nombre_superheroe_buscado, "no está en la lista de personajes.")

# b. Almacenar los superhéroes que pertenezcan al grupo "Guardianes de la galaxia" en una cola
cola_guardianes = deque()
for personaje in avengers:
    if personaje[2] == "Guardianes de la galaxia":
        nombre_superheroe = personaje[0]
        cola_guardianes.append(nombre_superheroe)
cantidad_guardianes = len(cola_guardianes)
print("Superhéroes en el grupo 'Guardianes de la galaxia':", list(cola_guardianes))
print("Cantidad de superhéroes en el grupo:", cantidad_guardianes)

# c. Mostrar de manera descendente los superhéroes que pertenecen a "Los cuatro fantásticos" y "Guardianes de la galaxia"
superheroes_fantasticos_guardianes = []
for personaje in avengers:
    grupo = personaje[2]
    if grupo == "Los cuatro fantásticos" or grupo == "Guardianes de la galaxia":
        nombre_superheroe = personaje[0]
        superheroes_fantasticos_guardianes.append(nombre_superheroe)
superheroes_fantasticos_guardianes.sort(reverse=True)
print("Superhéroes que pertenecen a 'Los cuatro fantásticos' o 'Guardianes de la galaxia' de manera descendente:")
for superheroe in superheroes_fantasticos_guardianes:
    print(superheroe)

# d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960
superheroes_posterior_1960 = []
for personaje in avengers:
    nombre_personaje = personaje[1]
    año_aparicion = personaje[3]
    if nombre_personaje != "" and año_aparicion > 1960:
        superheroes_posterior_1960.append(personaje[0])
print("Superhéroes con nombre de personaje cuyo año de aparición es posterior a 1960:")
for superheroe in superheroes_posterior_1960:
    print(superheroe)

# e. Modificar el superhéroe "Vlanck Widow" a "Black Widow"
for i, personaje in enumerate(avengers):
    if personaje[0] == "Vlanck Widow":
        avengers[i] = ("Black Widow", personaje[1], personaje[2], personaje[3])

# f. Agregar personajes de la lista auxiliar a la lista principal si no están cargados
lista_auxiliar = ['Black Cat', 'Hulk', 'Rocket Racoonn', 'Loki']
for personaje_auxiliar in lista_auxiliar:
    encontrado = False
    for personaje in avengers:
        if personaje[0] == personaje_auxiliar:
            encontrado = True
            break
    if not encontrado:
        avengers.append((personaje_auxiliar, "", "", 0))

# g. Mostrar todos los personajes que comienzan con C, P o S
letras_permitidas = ['C', 'P', 'S']
personajes_letras_permitidas = []
for personaje in avengers:
    nombre_superheroe = personaje[0]
    if nombre_superheroe[0] in letras_permitidas:
        personajes_letras_permitidas.append(nombre_superheroe)
print("Personajes que comienzan con C, P o S:")
for personaje in personajes_letras_permitidas:
    print(personaje)

# h. Cargar al menos 20 superheroes a la lista
avengers.append(("Ant-Man", "Scott Lang", "", 1979))
avengers.append(("Wasp", "Hope van Dyne", "", 1963))
avengers.append(("Falcon", "Sam Wilson", "", 1969))
avengers.append(("Winter Soldier", "Bucky Barnes", "", 2005))
avengers.append(("Doctor Strange", "", "", 1963))
avengers.append(("Black Bolt", "", "", 1965))
avengers.append(("Medusa", "", "", 1965))
avengers.append(("Quicksilver", "Pietro Maximoff", "", 1964))
avengers.append(("She-Hulk", "Jennifer Walters", "", 1980))
avengers.append(("Spider-Man", "Peter Parker", "", 1962))
avengers.append(("Green Goblin", "Norman Osborn", "", 1964))
avengers.append(("Venom", "Eddie Brock", "", 1984))
avengers.append(("Cyclops", "Scott Summers", "", 1963))
avengers.append(("Jean Grey", "", "", 1963))
avengers.append(("Beast", "Hank McCoy", "", 1963))
avengers.append(("Iceman", "Bobby Drake", "", 1963))
avengers.append(("Gambit", "Remy LeBeau", "", 1990))
avengers.append(("Storm", "Ororo Munroe", "", 1975))
avengers.append(("Colossus", "", "", 1975))
avengers.append(("Nightcrawler", "Kurt Wagner", "", 1975))
print("\nLista principal de personajes actualizada:")
for personaje in avengers:
    print(personaje)