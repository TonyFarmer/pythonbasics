from catclass import Cat
from dogclass import Dog

cat1 = Cat("Барон", "Мальчик", 2)
cat2 = Cat("Сэм", "Мальчик", 2)

dog1 = Dog("Мухтар", "Мальчик", 0)

print(cat1.get_info())
print(cat2.get_info())
print(dog1.get_info())