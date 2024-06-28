# def  fact(n):
#     a=2*n
#     b=n+1
#     if n==0 or n==1 :
#         return 1
#     else:
#         return (a*fact(a-1))// (b*fact(b-1)*n*fact(n-1))
# def fact1(n):
#     return fact(n)
# n=int(input("enter no of nodes"))
# print(fact1(n))
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        a = 2 * n
        b = n + 1
        c = (a * fact(a - 1)) 
        d = (b * fact(b - 1) * n * fact(n - 1))
        return c // d

def fact1(n):
    return fact(n)

n = int(input("Enter the number of nodes: "))
print(fact1(n))
