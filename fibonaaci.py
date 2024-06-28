#fibonacci series
n=int(input("Enter the no of fibonaaci numbers: "))
# a = [0] * (n + 1) #array initialization
# a[0]=1
# a[1]=1
# for i in range (2,n+1):
#     a[i]=a[i-1]+a[i-2]
#     print(a[i])
a=1
b=1
print(a,b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)

#using recursive function
def fib(n):
    #Base condition
    if n==1 or n==2:
        return 1
    
    #Decomposition
    a=fib(n-1)
    b=fib(n-2)

    #Recomposition
    return a+b
N = int(input("Nth fibonacci: "))
print(fib(N))


