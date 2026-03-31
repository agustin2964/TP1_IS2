from factorial_OOP import factorial

factorial=factorial()
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

factorial.run(num1,num2)