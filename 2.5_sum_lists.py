# Not writing iterative solution - recursive solution, pass back power of 10 as counter
import pdb
from linked_list_obj import Node, LinkedList

n1 = Node(5)
n2 = Node(8)
n3 = Node(7)
n4 = Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
l1 = LinkedList(n1)



def sum_lists_recursive(node_1, node_2, carry=0):
  dummy_node = Node(0)
  if not node_1 and not node_2:
    return null
  value = carry
  if node_1:
    value += node_1.val
  if node_2:
    value += node_2.val
  else:
    dummy_head.next = sum_lists_recursive(node_1.next, node_2.next, carry) % 10


