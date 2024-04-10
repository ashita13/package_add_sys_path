class Flower:
    
    color = "red"

    def __init__(self, ncolor=None):
        if ncolor is not None:
            self.color = ncolor

    @classmethod   
    def setColor(self, new_color):
        self.color = new_color
        
    def getColor(self):
        return self.color
        