for n in range(20,51):
    print(n,end=' ') if all(n%i for i in range(2,int(n**0.5)+1)) and n>1 else None