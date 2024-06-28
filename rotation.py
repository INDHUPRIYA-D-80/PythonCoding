# 1. Understand how LLs are created
# 2. CRUD operation
# 3. Loops in LLs 
# 4. Sort the LLs (merge sort)
# 5. Intersection in LLs 
# 6. Some interesting problems 

#Recall:Every class : Data + Function

class Node: #creating set of rules on every class creation
    #Data 
    def __init__(self, data): #for class frst keyword is self (its ignored)
        self.data = data
        self.next = None 

class LinkedList:

    #Data
    def __init__(self):
        self.head = None
    
    #Functions
    def append(self, data):
        new_node = Node(data)
        # If my head is empty
        if self.head is None:
            self.head = new_node
            return
        # If head is not empty
        last_node = self.head


        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # def left_rot(self,head):
    #     frst_node =self.head

    #     current=self.head.next
    #     self.head.next = None

    #     while current:
    #         if current.next!=None:
    #             current = current.next
    #             return current
    #         elif current.next==None:
    #             current.next = frst_node
    #             return current 
    #         else:
    #             return frst_node
    def left_rot(self):
        if self.head is None or self.head.next is None:
            return
       
        first_node = self.head #initialising the first node 
        current = self.head.next #making the second element as their frst element
        self.head = current #now making the frst element (previously second element) is now made as current 
        

        while current.next: #for every element thet has next element 
           current = current.next 
        
        # print(current.data,end=" ")
        # while current.next==None:
        #     current.next = first_node
        #     print(current.next)
        # self.head = self.head.next
        
        current.next = first_node
        #return current.next
        first_node.next = None
    
    def print(self):
        a= self.head
        while a:
            print(a.data, end=" ")
            a=a.next #DO NOT FORGET TO STEP FORWARD
        print()

l =LinkedList()
for i in range(1, 10):
    l.append(i)
l.print()
n =int(input("Enter the no.of.rotation "))
for i in range(n):
    l.left_rot()
    l.print()

    