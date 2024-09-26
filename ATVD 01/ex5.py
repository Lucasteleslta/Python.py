a = float(input("digite o valor de A: "))
b = float(input("digite o valor de B: "))
c = float(input("digite o valor de C: "))

delta = (b ** 2) - (4*a*c)

if (delta > 0): 
    print("Não tem raízes reais")

elif(delta == 0):  
    x = (- b) / (2*a)
    print("o valor das raízes são iguais, portanto o valor é: ", x)
   
else:
    x1 = (-b + delta ** 0.5) / (2*a)
    x2 = (-b - delta ** 0.5) / (2*a)
    print ("valor da primeira raíz é: ", x1)
    print ("valor da segunda raíz é: ", x2) 