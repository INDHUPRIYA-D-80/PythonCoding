# ~~1. Understand how LLs are created.~~
# ~~2. CRUD operations~~
# ~~3. Loops in LLs~~
# ~~4. Sort the LLs (merge sort)~~
# ~~5. Intersection in LLs~~
# 6. Some interesting problems

# Recall: Every class: Data + Functions
class Node:
    # Data
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Data
    def __init__(self):
        self.head = None

    # Functions
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

    # def get_nth_from_end(self, n):
    #     if not self.head:
    #         return None
        
    #     slow = self.head
    #     fast = self.head

    #     for i in range(n):
    #         if not fast:
    #             print("Error! Out of bounds!")
    #             return None
    #         fast = fast.next

    #     while fast:
    #         fast = fast.next
    #         slow = slow.next

        # # Slow is at nth last position
        # return slow.data
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
    
        self.head = prev

    def print(self):
        a = self.head
        while a:
            print(a.data, end=" ")
            a = a.next  # DO NOT FORGET TO STEP FORWARD
        print()


l = LinkedList()
# l2 = l.copy()
for _ in range(1, 12):
    l.append(_)

l.print()



l.reverse()
l.print()
print("Checking whether the linked list is palindrome or not:",end=" ")
print(l.reverse()==l)