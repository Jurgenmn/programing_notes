class Todo:
    def __init__(self, todo, id):
        self.txt = todo
        self.id = id

    def log_info(self):
        print(self.id, self.txt)
