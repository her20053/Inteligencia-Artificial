class Pixel:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.f = 0
        self.g = 0
    
    def __str__(self):
        if self.color == (255,0,0):
            return str('[Color: R' + ' Position: ' + str(self.position)+']')
        elif self.color == (0,255,0):
            return str('[Color: G' + ' Position: ' + str(self.position)+']')
        elif self.color == (0,0,0):
            return str('[Color: B' + ' Position: ' + str(self.position)+']')
        elif self.color == (255,255,255):
            return str('{Color: W' + ' Position: ' + str(self.position)+']')