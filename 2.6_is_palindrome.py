from linked_list_obj import Node, LinkedList

n1 = Node(5)
n2 = Node(6)
n3 = Node(7)
n4 = Node(6)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


def reverse_and_clone(head_node):
  curr_0 = head_node
  curr = Node(curr_0.val)
  prev = None
  nextt = None
  while curr_0.next:
    nextt = Node(curr_0.next.val)
    nextt.next = curr
    prev = curr
    curr = nextt
    curr_0 = curr_0.next
  return curr

def is_equal(head1, head2):
  curr1 = head1
  curr2 = head2
  while curr1.next and curr2.next:
    if curr1.val != curr2.val:
      return False
    curr1 = curr1.next
    curr2 = curr2.next
  if curr1.next or curr2.next:
    return False
  return True


def is_palindrome(head_node):
  rev_list_head = reverse_and_clone(head_node)
  return True if is_equal(head_node, rev_list_head) else False



print(is_palindrome(n1))