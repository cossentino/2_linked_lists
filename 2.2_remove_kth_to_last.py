from linked_list_obj import Node, LinkedList

n1 = Node(5)
n2 = Node(8)
n3 = Node(7)
n4 = Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
l1 = LinkedList(n1)


def k_to_last(l_list, k):
  runner = l_list.head
  trailer = l_list.head
  i = 0
  while runner.next and i < k:
    runner = runner.next
    i += 1
  trailer = trailer.next
  while runner.next:
    runner = runner.next
    trailer = trailer.next
  print(trailer.val)
  return trailer


# k_to_last(l1, 2)

# Recursive option (actually less optimal here)


def k_to_last_rec(l_list_head, k):
  if not l_list_head:
    return 0
  i = k_to_last_rec(l_list_head.next, k) + 1
  if i == k:
    print(f"{k}th to last node is {l_list_head.val}")
  return i

k_to_last_rec(l1.head, 3)