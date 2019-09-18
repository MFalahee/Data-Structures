# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

 # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  def insert(self, value):
    pass


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
    current = self.value

    while current:
      if target == current:
        return True
      else:
        if target < current:
          #go left if target is less than current
          current = current.left
        else:
          #go right
          current = current.right

    return False


 # * `get_max` returns the maximum value in the binary search tree.
 # go right until you can't go right
  def get_max(self):
    pass

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    pass