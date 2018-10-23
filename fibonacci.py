def fib():
    for x in range(2,n):
        f[x]=f[x-2]+f[x-1]
        f.append(f[x])

n=int(input('Enter number of fibonacci numbers: '))
#allocate numbers in list
f=[*range(n)]

fib()
print(f)

#one liner:
#fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
#fib(n)