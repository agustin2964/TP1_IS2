#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

#se ingresan los limites inferior y superior para calcular los factoriales
print("Ingrese el numero menor para calcular su factorial: ")
while True:
    try:
        num1=input()
        if num1=="":
            num1=1
            break
        else: 
            num1=int(num1)

            if num1>=0:
                break
            else:
                print("Ingrese un numero no negativo: ")
    except Exception as e:
        print("Error:", e)
        print("Ingrese un numero no negativo: ")
    
print("Ingrese el numero mayor para calcular su factorial: ")
while True:
    try:
        num2=input()   
        if num2=="":
            num2=60
            break
        else:
            num2=int(num2)
            if num2>=num1:
                break
    except:
        print("Ingrese un numero mayor o igual al anterior: ")
for i in range(num1,num2+1):
    print("Factorial ",i,"! es ", factorial(i))
