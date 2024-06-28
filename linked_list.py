#1. Understand how LLs are created
#2. CRUD operation
#3. Loops in LLs 
#4. Sort the LLs (merge sort)
#5. Intersection in LLs 
#6. Some interesting problems 

#Recall:Every class : Data + Function

def printlist(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

class Node: #creating set of rules on every class creation
    #Data 
    def __init__(self,data): #for class frst keyword is self (its ignored)
        self.data = data
        self.next = None
linked_list = Node(1)
linked_list.next = Node(2)
linked_list.next.next = Node(3)
linked_list.next.next.next = Node(4)

print(linked_list)

# class LinkedList:
#     def __init__(self):
