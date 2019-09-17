from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.storage = DoublyLinkedList()
    self.dict = {}
    self.limit = limit
    self.current_size = 0

  def find_node_move_front(self, key):
    found = False
    current = self.storage.head

    while current:
      if current.value == key:
        self.storage.move_to_front(current)
        found = True
      current = current.next
    
    return found
  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    #check the cache to see if it exists
    if key in self.dict:
      #If it exists, move it to the front in the order and return it
      self.find_node_move_front(key)
      return self.dict[key]

    else:
      return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):

    #if the list isn't full
      if self.current_size < self.limit:
        #update/add the key value pair in the cache
        self.dict.update({key: value})
        located = self.find_node_move_front(key)

        #if the key pair wasn't in the list already, we have to add it.
        if not located:
          self.storage.add_to_head(key)
          self.current_size += 1

    #if the list is full
      else:
        #update/add the key value pair in the cache
        self.dict.update({key: value})
        #look for key
        located = self.find_node_move_front(key)
        #if it was an update, we don't need to delete.
        #if it wasn't found, we have to delete the tail, and add the new key pair
        if not located:
          #grab oldest item, and delete it from the list and cache
          key_to_delete = self.storage.remove_from_tail()
          self.dict.pop(key_to_delete)
          #add new item
          self.storage.add_to_head(key)