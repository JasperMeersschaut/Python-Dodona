# https://dodona.be/nl/courses/4195/series/46772/activities/1394891023

class BinaryHeap:

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.arr=[]*self.max_size

    def empty(self):
        return len(self.arr)==0
    
    def get_min_elem(self):
        if not self.empty():
            return self.arr[0]

    def insert_elem(self, item):
        if len(self.arr) < self.max_size:
            index = len(self.arr)
            self.arr.append(item)
            while index >0 and item < self.arr[(index-1)//2]:
                self.arr[index],self.arr[(index-1)//2] = self.arr[(index-1)//2],item
                index = (index-1)//2

    def remove_min_elem(self):
        if not self.empty():
            root = self.arr[0]
            if len(self.arr)==1:
                self.arr.pop()
            else:
                self.arr[0] = self.arr.pop()
            index = 0
            while (index*2+1 <len(self.arr) and self.arr[index] < self.arr[index*2+1]) or (index*2+1 <len(self.arr) and self.arr[index] < self.arr[index*2+2]):
                minIndex = index*2+1
                if index*2+1 <len(self.arr) and self.arr[index*2+2] < self.arr[index*2+1]:
                    minIndex = index*2+2
                self.arr[index],self.arr[minIndex] = self.arr[minIndex],self.arr[index]
                index = minIndex
            return root

                

    def __str__(self):
        return str(self.arr)
