import math 

class Cyrcle:
    def __init__(self, r):
        self.r = r		  
    def get_area(self):		
        return math.pi*self.r**2
       
class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b		  
    def get_area(self):		
        return self.a * self.b
    def __eq__(self, other):
        return self.get_area() == other.get_area()
    	
class Square:
    def __init__(self,a):
        self.a = a
    def get_area_square(self):		
        return self.a ** 2
    
