def nombre(usuario, repeticiones):
    if repeticiones <= 0:
        return
    print(usuario)
    nombre(usuario, repeticiones - 1)

n_usuario = input("Escribe tu nombre: ")
n_repeticiones = int(input("Escribe un número entero: "))

nombre(n_usuario, n_repeticiones)