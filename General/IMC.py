print("Bienvenido a la calculadora de IMC")
print ("Ingrese su altura en metros")
altura = float(input())
print("Ingrese su peso en kilos")
peso = float(input())

IMC = (peso / (altura * altura))

if IMC < 18.5:
    print("Su IMC es de " + str(IMC) + " por lo que está bajo de peso considerado normal")
elif 18.5 <= IMC < 24.9:
    print("Su IMC es de " + str(IMC) + " por lo que está en un peso ideal")
elif 25 <= IMC < 30:
    print("Su IMC es de " + str(IMC) + " por lo que pesa más de lo que es considerado normal")
elif IMC >= 30:
    print("Usted está obeso, vaya al gym")

