#binary_to_decimal
def btd(n):
     m=str(n)
     res=0
     for i in  m:
          res=res*2+int(i)
     print(res)
N=int(input())
btd(N)
