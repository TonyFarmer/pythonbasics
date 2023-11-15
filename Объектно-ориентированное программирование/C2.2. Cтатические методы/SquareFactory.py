class Square():
    def __init__(self, side):
        self.side = side

class SquareFactory():
    @staticmethod
    def SIDE(side):
        return Square(side)
    
square = SquareFactory.SIDE(21)

print(square.side)
