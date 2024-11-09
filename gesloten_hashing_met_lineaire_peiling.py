# https://dodona.be/nl/courses/4195/series/46773/activities/1385084508

from operator import indexOf
from sys import maxsize


class HashSet:
    flag= -9999
    def __init__(self, max_size=10):
        self.arr = [None]*max_size
        self.max_size = max_size
        self.nb = 0

    def add(self, item):
         if self.nb >= self.max_size:
            raise ValueError("Achterliggende array vol")
         index = hash(item)%self.max_size
         while self.arr[index] != None:
            print(index)
            index = (index+1)%self.max_size
         self.arr[index]=item
         self.nb += 1
         return index



    def index_of(self, item):
        index=hash(item) % self.max_size
        firstIndex = index
        while self.arr[index] is not None and item !=self.arr[index]:
            print(index)
            index = (index+1) % self.max_size
            if firstIndex == index:
                return index
            return -1

    def delete(self, item):
        index = self.indexOf(item)
        if index == -1:
            return False
        self.Arr[index] = HashSet.flag
        return True

