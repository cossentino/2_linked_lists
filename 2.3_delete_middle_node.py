from linked_list_obj import Node, LinkedList

n1 = Node(5)
n2 = Node(8)
n3 = Node(7)
n4 = Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
l1 = LinkedList(n1)


def delete_middle_node(node):
  runner = node.next
  trailer = node
  while runner:
    trailer.val = runner.val
    trailer = runner
    runner = runner.next
  
delete_middle_node(n2)
print(l1.head.val)
print(l1.head.next.val)
print(l1.head.next.next.val)