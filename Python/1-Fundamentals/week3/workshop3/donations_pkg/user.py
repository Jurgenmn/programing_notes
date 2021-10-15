"""def login(database, username, password):
    for key in database:
        if key == username and database[key] == password:
            print("Wellcome", username + "!")
            return username
        elif key == username and database[key] != password:
            print("Incorrect password for", database[key])
            return ""
    print("User not found")
    return """


def login(database, username, password):
    if username in database and password == database[username]:
        print("Wellcome", username + "!")
        return username
    elif username in database and password != database[username]:
        print("Incorrect password for", username)
        return ""
    else:
        print("User not found\n")
        return ""


def register(database, username):
    if username in database:
        print("Username already registerd")
        return ""
    else:
        print("Username " + username + " has been registerd")
        return username
