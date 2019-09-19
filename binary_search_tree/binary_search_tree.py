import sys
from dll_queue import Queue
from dll_stack import Stack

'''
Lecture Notes

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent

'''

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  
  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert

  def insert(self, value):
    #recursion is our friend
    if value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
      
    else:
      if self.right == None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
        
    


  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children

  def contains(self, target):
    #compare to value
    #if value = target, return true
    #if greater than or equal --->
    #if less <---
    #If no current value and target wasn't found return false.

    if self.value == target:
      return True
    else: 
      if target < self.value:
        if self.left == None:
          return False
        else:
          return self.left.contains(target)
      else:
        if self.right == None:
          return False
        else:
          return self.right.contains(target)


 # * `get_max` returns the maximum value in the binary search tree.
 # go right until you can't go right
  def get_max(self):
    if self.right == None:
      return self.value

    else:
      return self.right.get_max()


  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):

    cb(self.value)

    if self.right != None:
      self.right.for_each(cb) 

    if self.left != None:
      self.left.for_each(cb)

  # DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal

    # depth first --> go down (pick a direction) until we run into a dead end
    # once you hit a dead end, circle back one and go the other way
    # continue until we hit all of the nodes
    # depth first stack, sort the entries into the stack I'm guessing? Conditional of some sort.

  def in_order_dft(self, node):
      #check left side, recursively until we hit a dead end to the left (lowest number)
      if node.left is not None:
        node.left.in_order_dft(node.left)

      #Print value!
      print(node.value)

      #move right when the value is printed
      if node.right is not None:
        node.right.in_order_dft(node.right)


  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
      #print first node
      print(node.value)

      #initialize queue
      store = Queue()

      #add first values to queue
      if node.left is not None:
        store.enqueue(node.left)
      if node.right is not None:
        store.enqueue(node.right)

      while store.len() > 0:
        current_node = store.dequeue()
        print(current_node.value)

        if current_node.left is not None:
          store.enqueue(current_node.left)
        if current_node.right is not None:
          store.enqueue(current_node.right)

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  # when stack is empty, we have traversed the entire tree, we are done
  def dft_print(self, node):
      #print first node
      print(node.value)

      #initialize stack
      store = Stack()

      #push in first children so Stack isn't empty when we start iterating the loop
      if node.left is not None:
        store.push(node.left)
      if node.right is not None:
        store.push(node.right)

      while store.len() > 0:
        current_node = store.pop()
        print(current_node.value)

        if current_node.left is not None:
          store.push(current_node.left)
        if current_node.right is not None:
          store.push(current_node.right)







  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass
