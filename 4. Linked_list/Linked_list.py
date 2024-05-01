class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = Node(None)
  
  def insert(self, addr, data):
    newNode = Node(data)
    newNode.next = addr.next
    newNode.prev = addr
    if (addr.next): addr.next.prev = newNode
    addr.next = newNode 

  def erase(self, addr):
    if addr == self.head: return
    if (addr.next == None):
      addr.prev.next = None
      return
    
    addr.prev.next = addr.next
    addr.next.prev = addr.prev
  
  def traverse(self):
    cur = self.head.next

    while cur:
      print(cur.data, end=" ")
      cur = cur.next
    print()

class TestModule:
  def __init__(self):
    self.ll = LinkedList()

  def insert_test(self):
    head = self.ll.head
    print("***** insert test *****")
    self.ll.insert(head, 10); # 10
    self.ll.traverse();
    self.ll.insert(head, 30); # 30 10
    self.ll.traverse();
    self.ll.insert(head.next, 40); # 30 40 10
    self.ll.traverse();
    self.ll.insert(head.next.next.next, 20); # 30 40 10 20
    self.ll.traverse();
    self.ll.insert(head.next.next.next.next, 70); # 30 40 10 20 70
    self.ll.traverse();

  def erase_test(self):
    head = self.ll.head
    print("****** erase_test *****")
    self.ll.erase(head.next.next.next); # 30 40 20 70
    self.ll.traverse();
    self.ll.erase(head.next); # 40 20 70
    self.ll.traverse();
    self.ll.erase(head.next.next); # 40 70
    self.ll.traverse();
    self.ll.erase(head.next.next); # 40
    self.ll.traverse();

module = TestModule()
module.insert_test()
module.erase_test()

