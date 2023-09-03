print("Escriba un correo electronico: ")
correo = input(": ")
option_one = "gmail"
replace_one = "ceu"
option_two = ".com"
replace_two = ".es"
newcorreo1 = correo.replace(option_one, replace_one)
new_correo2 = newcorreo1.replace(option_two, replace_two)

print(new_correo2)