class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return f"Rectangle : {self.a}, {self.b}"
    

rec1 = Rectangle(1, 5)

print(rec1)