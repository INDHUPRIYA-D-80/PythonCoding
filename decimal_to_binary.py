#decimal to binary conversion
n=int(input("Enter the decimal number:"))
k=0
# for i in range (0,n//2):
#     if (n==1):
#         k=k
#     else
        
# for i in range(0,n//2):

c=[]#initialising the list
while n>0:
    b=n%2
    n=n//2
    #appending the each remainder
    c.append(b) 

#reversing the list 
print(c[::-1]) 




#decimal_to_binary(dtb)
# explanation for 70 answer:- 1000110
# dtb(70)  
# dtb(35)+"0"
# dtb(17)+"1"+"0"
# dtb(8)+"1"+"1"+"0"
# dtb(4)+"0"+"1"+"1"+"0"
# dtb(2)+"0"+"0"+"1"+"1"+"0"
#"10"+"0"+"0"+"1"+"1"+"0"