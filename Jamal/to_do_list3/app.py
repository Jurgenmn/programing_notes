from todo_pkg.todo import Todo


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
        your_todo = input("Add your todo: ")
        todo = Todo(id, your_todo)  #
        id += 1
        todo_list.append(todo)
    elif option == "4":
        for todo in todo_list:
            todo.show_todo()  # print(todo)

    elif option == "2":
        selected_todo = int(
            input("Select the id of todo you want to delete: "))
        for todo in todo_list:
            if todo.id == selected_todo:
                todo_list.remove(todo)

    elif option == "3":
        selected_todo = int(input("Which todo you want update (id) "))
        updated_todo = input("Update your todo: ")
        for todo in todo_list:
            if todo.id == selected_todo:
                todo.txt = updated_todo

    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option chose from 1 to 5")
