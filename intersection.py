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

    def find_intersection(self, head2):
        visited = set()

        current = self.head
        while current:
            visited.add(current)
            current = current.next

        current = head2.head
        while current:
            if current in visited:
                return current
            current = current.next

        return None

    def print(self):
        a = self.head
        while a:
            print(a.data, end=" ")
            a = a.next  # DO NOT FORGET TO STEP FORWARD
        print()


l1 = LinkedList()

intersection_node = Node(4)

l1.append(1)
l1.append(2)
l1.append(3)
l1.head.next.next.next = intersection_node
l1.append(6)
l1.append(8)

l2 = LinkedList()

l2.append(2)
l2.head.next = intersection_node

l1.print()
l2.print()

ins_node = l1.find_intersection(l2)
print(ins_node.data, ins_node)