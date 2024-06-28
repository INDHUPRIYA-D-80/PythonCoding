#PS:Distance between two points


#Input:
#x1 y1
#x2 y2
        
#output
# Distance between two points
#x1,y1,x2,y2 = list(map(int, input().split())) #getting inputs in a single line
#x2,y2 = list(map(int, input().split()))

# distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
# print(distance)


#PS:points in, out or on the circle

#Input:
#x1 y1 r
#x2 y2
        
#output
#Inside/Outside/On the circle

# x1,y1,r = list(map(int, input().split())) #getting inputs in a single line
# x2,y2 = list(map(int, input().split()))

# d = ((x2-x1)**2 + (y2-y1)**2)**0.5

# if d>r:
#     print("Outside the circle")
# elif d<r:
#     print("Inside the circle")
# else:
#     print("Onthe circle")



#PS:points in, out or on the circle
#Input:
#a b c
        
#output: Side angle Triangle
# sides = ["Equi","Iso","Scalen"]
# angles = ["Right","Obtuse","Acute"]
#print: Not a valid triangle
'''
import math
a,b,c = list(map(int, input().split())) #getting inputs in a single line
if a + b > c and a + c > b and b + c > a:  #if the sides are negative or zero then it doesn't form a triangle
    print("Not a valid triangle",end="")
else:
    if (a==b)and (b==c)and (a==c):
        print("It's an Equilateral",end="")
    elif (a==b)or(b==c)or(a==c):
        print("It's an isosceles",end="")
    else:
        print("Its scalene triangle",end="")

A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
C = 180 - A - B  # Sum of angles in a triangle is 180 degrees

if A < 90 and B < 90 and C < 90:
    print(" and acute angled triangle") #if a**2 + b**2 <0
elif A > 90 or B > 90 or C > 90:
    print(" and obtuse angled triangle")#if a**2 + b**2 >0
else:
    print(" and Right angled triangle") #if a**2 + b**2 =0
'''
a,b,c = list(map(int, input().split())) 
s=a+b+c
if s-a<0 or s-b<0 or s-c<0:  
  print("Not a valid triangle",end="")
else:
    if (a==b)and (b==c)and (a==c):
        print("It's an Equilateral",end="")
    elif (a==b)or(b==c)or(a==c):
        print("It's an isosceles",end="")
    else:
        print("Its scalene triangle",end="")
if a*a + b*b <c*c:
  print(" and acute angled triangle") 
elif a*a + b*b >c*c:
  print(" and obtuse angled triangle")
else:
  print(" and Right angled triangle") 
