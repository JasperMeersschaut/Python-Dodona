# https://dodona.be/nl/courses/4195/series/46774/activities/936085588

class QueueList:

    class Knoop:
        def __init__(self, data = None, volgende =None):
            self.data = data
            self.volgende= volgende


    def __init__(self):
        self.kop = None
        self.staart = None

    def empty(self):
        return self.kop is None

    def enqueue(self, data):
        hulp = QueueList.Knoop(data)
        if self.empty():
            self.kop = hulp
        else:
            self.staart.volgende = hulp
        self.staart = hulp

    def front(self):
        if self.kop is not None:
            return self.kop.data
        return None
    
    def dequeue(self):
        if self.kop is not None:
            temp = self.kop.data
            self.kop = self.kop.volgende
            if self.kop is None:
                self.s = None
            return temp

    def invert(self):
        vorige = None
        huidige = self.kop
        while huidige is not None:
            volgende = huidige.volgende
            huidige.volgende = vorige
            vorige = huidige
            huidige = volgende
        self.kop = vorige

# class QueueList:
#     class Knoop:
#         def __init__(self, data=None, volgende=None):
#             self.data = data
#             self.volgende = volgende

#     def __init__(self):
#         self.k = None
#         self.s = None

#     def empty(self):
#         return self.k is None

#     def enqueue(self, x):
#         hulp = QueueList.Knoop(x)
#         if self.empty():
#             self.k = hulp
#         else:
#             self.s.volgende = hulp
#         self.s = hulp

#     def dequeue(self):
#         if self.empty():
#             return None
#         x = self.k.data
#         if self.k == self.s:
#             self.k = None
#             self.s = None
#         else:
#             self.k = self.k.volgende
#         return x

#     def front(self):
#         if self.empty():
#             return None
#         return self.k.data
#     def invert(self):
#         vorige=None
#         ref = self.k
#         while ref Is None
