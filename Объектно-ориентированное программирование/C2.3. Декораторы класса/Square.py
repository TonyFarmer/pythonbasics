# Создать вычисляемое свойство для класса Square. 
# Сделайте метод по вычислению площади свойством. 
# Сделайте сторону квадрата свойством, которое можно установить только через сеттер. 
# В сеттере добавьте проверку условия, что сторона должна быть неотрицательной.

class Square():
    _side = None

    @property
    def square(self):
        return  self._side**2 if self._side != None else "None"
    
    @square.setter
    def side(self, side):
        if side > 1:
            self._side = side
        else:
            print("Side should be higher then 0")

sq = Square()
sq.side = 0
print(sq.side)



