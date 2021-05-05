from linked_list_obj import Node, LinkedList
import pdb

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6


# Reverse a linked list!! Did ittt:

# curr = n1
# prev = None
# nextt = None

# while curr:
#   nextt = curr.next
#   curr.next = prev
#   prev = curr
#   curr = nextt


# Clone a new reversed copy of the linked list!! did ittttt: 

# curr_0 = n1

# curr = Node(curr_0.val)
# prev = None
# nextt = None


# while curr_0.next:
#   nextt = Node(curr_0.next.val)
#   nextt.next = curr
#   prev = curr
#   curr = nextt
#   curr_0 = curr_0.next
  
  
# pdb.set_trace()










