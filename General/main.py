print("Ingresa tu salario")
salario = input()
salarioDecimal = float(salario)

necesidades = salarioDecimal * 0.5
deseos = salarioDecimal * 0.3
inversiones = salarioDecimal * 0.2

print("Tu salario de " + str(salarioDecimal) + " los cuales son " + str (necesidades) + " necesidades, " + str(deseos) + " deseos, " + str(inversiones) + " inversiones" )
