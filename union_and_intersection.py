class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head.next:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += str(cur_head.value)
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    if type(llist_1) != LinkedList or type(llist_2) != LinkedList or (llist_1.size() == 0 and llist_2.size() == 0):
        return None
    else:
        lst = list()
        llist_union = LinkedList()
        
        #Traversing through first linked list
        current_node = llist_1.head
        while current_node:
            if current_node.value not in lst:
                lst.append(current_node.value)
            current_node = current_node.next
        
        #Traversing through second linked list
        current_node = llist_2.head
        while current_node:
            if current_node.value not in lst:
                lst.append(current_node.value)
            current_node = current_node.next
            
        lst.sort()
        
        #We have to create a new linked list with the above sorted list
        for element in lst:
            llist_union.append(element)
        
        if llist_union.head != None:
            return llist_union
        else:
            return None

def intersection(llist_1, llist_2):
    if type(llist_1) != LinkedList or type(llist_2) != LinkedList or llist_1.size() == 0 or llist_2.size() == 0:
        return None
    else:
        lst1 = list()
        lst2 = list()
        llist_intersection = LinkedList()
        
        #Traversing through first linked list
        current_node = llist_1.head
        while current_node:
            if current_node.value not in lst1:
                lst1.append(current_node.value)
            current_node = current_node.next
        
        #Traversing through second linked list
        current_node = llist_2.head
        while current_node:
            if current_node.value not in lst2:
                lst2.append(current_node.value)
            current_node = current_node.next
            
        lst1.sort()
        
        for element in lst1:
            if element in lst2:
                llist_intersection.append(element)
        
        if llist_intersection.head != None:
            return llist_intersection
        else:
            return None

#-----------------TEST CASES---------------------
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("TEST CASE 1")
print (union(linked_list_1,linked_list_2))
# prints 1 -> 2 -> 3 -> 4 -> 6 -> 9 -> 11 -> 21 -> 32 -> 35 -> 65

print (intersection(linked_list_1,linked_list_2))
# prints 4 -> 6 -> 21


linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("\nTEST CASE 2")
print (union(linked_list_3,linked_list_4))
# prints 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 35 -> 65

print( intersection(linked_list_3,linked_list_4))
# prints None

print("\nTEST CASE 3")
print(union(1, 3))
# prints None

print(intersection(1, 3))
# prints None

print("\nTEST CASE 4")
print(union(None, None))
# prints None

print(intersection(None, None))
# prints None

print("\nTEST CASE 5")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
print(union(linked_list_5, linked_list_6))
#prints None

print(intersection(linked_list_5, linked_list_6))
#prints None

print("\nTEST CASE 6")
print(union(linked_list_5, linked_list_4))
#prints 1 -> 7 -> 8 -> 9 -> 11 -> 21

print(intersection(linked_list_5, linked_list_4))
#prints None