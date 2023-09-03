print ("Escribe tú número de teléfono en el formato +34-XXXXXX-XX: ")

cel = input(": ")

parts = cel.split("-")
prefijo = parts[1]

print( " Tú Número de teléfono sin prefijo y extensión: ", prefijo)