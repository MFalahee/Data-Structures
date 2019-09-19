import sys
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()


#adds an item to the back of the queue
  def enqueue(self, value):
    self.storage.add_to_tail(value)
  
#removes and returns an item from the front of the queue
  def dequeue(self):
      return self.storage.remove_from_head()

#returns the number of items in the queue
  def len(self):
    return self.storage.length
