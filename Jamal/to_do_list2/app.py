from todos_pkg.todo import Todo


def interface():

    print("1)  ADD TODO")
    print("2)  DELETE TODO")
    print("3)  UPDATE TODO")
    print("4)  SHOW TODO")
    print("5)  QUIT")


todo_list = []
id = 0

while True:
    interface()

    option = input("Choose option: ")
    if option == "1":
        todo_text = input("What's your to do? ")
        todo = Todo(todo, id)
        id += 1
        todo_list.append(todo)

    elif option == "4":
        for todo in todo_list:
            todo.show_todo()

    elif option == 2:
        todo_id = int(input("Which id do yo want to delete?"))
        for todo in todo_list:
            if todo.id == todo_id:
                123
