from todos.todo import Todo


def interface():

    print("1)   ADD TODO")
    print("2)   DELETE TODO")
    print("3)   UPDATE TODO")
    print("4)   SHOW TODO")
    print("5)   Quit")


todo_list = []
id = 0

while True:
    interface()
    option = input("Select option: ")
    if option == "1":
        txt = input("Todo: ")
        todo = Todo(txt, id)
        id += 1
        todo_list.append(todo)

    elif option == "4":
        for todo in todo_list:
            todo.log_info()

    elif option == "2":
        todo_id = int(input("Id: "))
        for todo in todo_list:
            if todo.id == todo_id:
                todo_list.remove(todo)

    elif option == "3":
        todo_id = int(input("ID: "))
        for todo in todo_list:
            if todo.id == todo_id:
                update_todo = input("Update: ")
                todo.txt = update_todo
    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Wrong input")
        continue
