# Создадим класс Queue — нужная нам очередь
class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди
    

    # !!! Класс далее нужно дополнить методами !!!
    def size(self):
        if self.is_empty():  # если она пуста
            return 0  # возвращаем ноль
        elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
            return self.max_size  # значит очередь заполнена
        if self.head > self.tail:
            return self.tail + self.max_size - self.head
        elif self.tail > self.head:
            return self.tail - self.head

    def add(self):
        self.task_num += 1  # увеличиваем порядковый номер задачи
        self.tasks[self.tail] = self.task_num  # добавляем его в очередь
        print(f"Задача №{self.tasks[self.tail]} добавлена")

        # увеличиваем указатель на 1 по модулю максимального числа элементов
        # для зацикливания очереди в списке
        self.tail = (self.tail + 1) % self.max_size

    def show(self):
        print(f"Задача {self.tasks[self.head]} в приоритете")
    
    def pop(self):
        self.tasks[self.head] = 0
        if self.head == 0 and self.tail == self.max_size:
            self.head += 1
            self.tail = 0
        elif self.head == self.max_size - 1:
            self.head = 0
        else: 
            self.head += 1

    def is_empty(self):
        return self.head == self.tail and self.tasks[self.head] == 0
        
    def do(self):  # выполняем приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} выполнена")
        # после выполнения зануляем элемент по указателю
        self.pop()
        # и циклично перемещаем указатель

# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty": 
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add": 
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show": 
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do": 
        print(q.size())
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit": 
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")
