import matplotlib.pyplot as plt
valores=[]
for i in range(1,10001):
    c=0
    num=i
    while num not in [1,2,4]:
        if num%2==0:
            num=num//2
        else:
            num=3*num+1
        c+=1
    valores.append(c)
print(valores)

plt.plot(range(1, 10001), valores)
plt.xlabel("Número inicial")
plt.ylabel("Iteraciones")
plt.title("Conjetura de Collatz (1 a 10000)")
plt.show()