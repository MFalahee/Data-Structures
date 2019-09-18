# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

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
      


