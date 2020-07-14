#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'ruthmayodi'


class Node:
    def __init__(self, key, value=None):
        """To initialize the the class Node"""
        self.hash = hash(key)
        self.key = key
        self.value = value
        
        return 
    
    def __repr__(self):
        """To invoke the object"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'


    def __eq__(self, other):
        """To return a comparison"""
        return self.hash == other.hash and self.key == other.key



class NoDict:
    def __init__(self, num_buckets=10):
        """initializer to create the buckets according to a size parameter"""
        self.size = num_buckets
        self.buckets = [ [] for _ in range(num_buckets) ]
        

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' 
                           for i, bucket in enumerate(self.buckets)])


    def add(self, key, value):
        """accept a new key and value, and store it into the `NoDict` instance. 
        This method should not allow duplicate keys."""
        new_node = Node(key, value)
        current_bucket = self.buckets[new_node.hash % self.size]
        for node in current_bucket:
            if node == new_node:
                current_bucket.remove(node)
                break
        current_bucket.append(new_node)

        

    def get(self, key):
        """This class method should perform a key-lookup in the `NoDict` class"""
        node_to_find = Node(key)
        current_bucket = self.buckets[node_to_find.hash % self.size]
        for node in current_bucket:
            if node == node_to_find:
                return node.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """This will make the class behave more like a regular dictionary"""
        
        return self.get(key)

    def __setitem__(self, key, value):
        """To enable square-bracket _assignment_ behavior"""
        
        return self.add(key, value)
