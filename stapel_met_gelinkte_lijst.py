# https://dodona.be/nl/courses/4195/series/46774/activities/2064046031

class StackList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.top = None

    def empty(self):
        return self.top is None

    def push(self, data):
        hulp = StackList.Knoop()
        hulp.data = data
        hulp.volgende=self.top
        self.top=hulp

    def peek(self):
        return self.top.data

    def pop(self):
        if self.top is None:
            return None
        x= self.top.data
        self.top = self.top.volgende
        return x
        
