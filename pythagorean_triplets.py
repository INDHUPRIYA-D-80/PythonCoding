#Problem Statement :Upto N, Ineed to find all (a,b,c) triplets
#Also, I want to have a count of them.

N = int(input("Enter the value of N:"))
count = 0 # initialising count as zero

#LOOPING
#range(x,y) = start from x,go upto y-1
#IF range (1,9) then its start from 1 and goes until 8

for a in range(1,N+1):
    for b in range(a,N+1): # b should be greater than b
        for c in range(b,N+1):
            if c*c == (a*a + b*b):
                print(a,b,c)
                count =count+1 #incrementing the count value for every triplets found

print("Total Triplets Found: ",count)