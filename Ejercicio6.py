print ("Escribe una Frase: ")
frass = input (": ")

print ("Escribe una Vocal: ")
voca= input(": ")
modificada = frass.replace(voca, voca.upper())

print("Frase Modificada:", modificada)