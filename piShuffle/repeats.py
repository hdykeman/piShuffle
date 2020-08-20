class repeatList:
    def __init__(self, length):
        self.data = []
        self.length = length

    def add(self, track):
       #print(track)
       if len(self.data) >= self.length:
           self.data.pop()
       self.data.insert(0, track)