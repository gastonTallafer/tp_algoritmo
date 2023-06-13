def contar_palabra(vector, palabra):
    if len(vector) == 0:
        return 0
    if vector[0] == palabra:
        return 1 + contar_palabra(vector[1:], palabra)
    else:
        return contar_palabra(vector[1:], palabra)

# Ejemplo de uso
vector_palabras = ["hola", "mundo", "hola", "hola", "adios"]
palabra_buscada = "hola"

contador = contar_palabra(vector_palabras, palabra_buscada)
print("La palabra", palabra_buscada, "aparece", contador, "veces en el vector.")