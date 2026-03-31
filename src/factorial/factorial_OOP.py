class factorial:
    def __init__(self):
        pass

    def run(self, min, max):
        for i in range(min, max+1):
            if i < 0: 
                print("Factorial de un número negativo no existe")
            elif i == 0: 
                print(f"el factorial {i}! es 1") 
                
            else: 
                num = i
                fact = 1
                while(num > 1): 
                    fact *= num 
                    num -= 1
                print(f"el factorial {i}! es {fact}") 