for i in range(1,10001):
    c=0
    num=i
    while num not in [1,2,4]:
        if num%2==0:
            num=num//2
        else:
            num=3*num+1
        c+=1
    print(f"{i} {c}")