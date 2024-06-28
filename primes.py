#Problem Statement : Count all the primes from M to N. Print all those Primes

M = int(input("Enter the Starting Number: \n"))
N = int(input("Enter the Ending Number: \n"))

count = 0 # initialising count as zero

#function for checking a value is prime or not
#JUMPING
def is_prime(x):
    for a in range(2,x):
        if x%a == 0:
            #Not a Prime
            return False
    #This is prime
    return True
    
for i in range(M, N+1):
    #print(i)
    if is_prime(i):
        count = count+1
        print(i)
print("Total Prime Numbers: ",count)
