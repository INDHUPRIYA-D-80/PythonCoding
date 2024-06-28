#PROBLEM STATEMENT IMAGINE A LIST WITH RANDOM NUMBERS EXAMPLE[34,7,91,9,1,20,10,3,32] WHAT IS THE MAXIMUM NUMBER 
# YOU CAN CREATE BY ATTACHING CONNECTING ELEMENTS OF THIS ARRAY EXPECTED AS 9 91 7 34 20 1 10 3 32 => 99173420110
elements = [34,7,91,9,1,20,10]
elements2 = []

for i in range(len(elements)):
    elements2.append(str(elements[i]))

def double_num(x):
     return x*2
print(sorted(elements2))# output will be ['1', '10', '20', '34', '7', '9', '91'] only for sorting elements2 without touching it.
elements2.sort(key=double_num,reverse=True) 

print(elements2) 

print("".join(elements2))

