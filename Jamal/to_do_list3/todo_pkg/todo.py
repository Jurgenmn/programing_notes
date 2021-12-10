class Todo:
    def __init__(self, id, todo):
        self.id = id
        self.txt = todo

    def show_todo(self):
        print(self.id, self.txt)
