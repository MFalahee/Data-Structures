import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()


#adds an item to the back of the queue
  def enqueue(self, value):
    pass
  
#removes and returns an item from the front of the queue
  def dequeue(self):
    pass

#returns the number of items in the queue
  def len(self):
    pass
