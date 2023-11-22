class Test():
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("The end of file")
        self.file.close()


with Test("test.txt", "r") as t:
    print(t.read())
