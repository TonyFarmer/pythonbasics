from catclass import Cat

class Dog(Cat):
    def get_info(self):
        return self.name, self.age
    