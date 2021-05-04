class Node():

  def __init__(self, data, nextt = None):
    self.val = data
    self.next = nextt


class LinkedList():

  def __init__(self, head = None):
    self.head = head