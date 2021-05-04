# Write code to remove duplicates from an unsorted linked list.
# Follow up - how would you solve if a temporary buffer is not allowed?

from linked_list_obj import Node, LinkedList

"""Brute force: walk through linked list. At each node in linked list, start from beginning and remove nodes equal to that node"""

n1 = Node(5)
n2 = Node(7)
n3 = Node(7)
n4 = Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
l1 = LinkedList(n1)

def remove_dups(l_list, memo={}):

  if l_list.head and l_list.head.next:
    pointer = l_list.head
    memo[pointer.val] = 0
    pointer_prev = pointer
    pointer = pointer.next
    while pointer.next:
      try:
        memo[pointer.val] += 1
        pointer_prev.next = pointer.next
        pointer = pointer.next
        print('Pointer', pointer.val)
        print('PointerPrev', pointer_prev.val)
      except KeyError:
        memo[pointer.val] = 0
        pointer_prev = pointer
        pointer = pointer.next
        print('Pointer', pointer.val)
        print('PointerPrev', pointer_prev.val)
  print_pointer = l1.head
  while print_pointer.next:
    print(print_pointer.val)
    print_pointer = print_pointer.next
  print(print_pointer.val)
  return l_list


remove_dups(l1)


# My sol = book sol = hash table
# If no hash table allowed, use second pointer and run through list