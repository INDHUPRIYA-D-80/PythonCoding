#list = ["1","2","4","5","6"]
n=int(input("Enter the no of elements : "))
list=[]
for i in range(0,n):
        list.append(input())
print(" ".join(sorted(list[-2])))