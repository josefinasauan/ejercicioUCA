import random


try:
    print("1) Contenido actual de lenguajes.txt:")
    with open("lenguajes.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except Exception as e:
    print("Error al leer lenguajes.txt:", e)


nuevos_lenguajes = ["go", "ruby"]

try:
    with open("lenguajes.txt", "a") as archivo:
        for lenguaje in nuevos_lenguajes:
            archivo.write(f"{lenguaje}\n")
    print("2) Nuevos lenguajes agregados al archivo:", ", ".join(nuevos_lenguajes), "\n")
except Exception as e:
    print("Error al escribir en lenguajes.txt:", e)


def generar_quini6():
    return sorted(random.sample(range(0, 46), 6))

resultados = generar_quini6()

print("3) Resultados del Quini 6:")
print("Números sorteados:", resultados)


try:
    with open("resultados.txt", "w") as archivo:
        archivo.write("Resultados del Quini 6:\n")
        archivo.write(", ".join(map(str, resultados)))
    print("\nArchivo 'resultados.txt' generado con éxito.")
except Exception as e:
    print("Error al guardar resultados.txt:", e)