# f2 = open("./password", "w")
f = open("./password", "r")

#print(f.name)

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()

#print(line1)
#print(line2)
#print(line3)
#f2.write("Hello World\n")
#f2.write("Jurgen, Jamal!!!")

#read
# what is the username: jur@gmail.com
#your passwerd is: 1234

def remove_newline(lines):
    new_list = []
    for i in lines:
        new_list.append(i[: -1])
    
    return new_list 

lines = f.readlines()
print(lines)
new_lines = remove_newline(lines)
print(new_lines) 


# userInput = input("Create or Read a new account?")
# if(userInput == "Create"):
#     accountName = input("Account Name: ")
#     password = input("Password: ")
#     f2.write(accountName + "\n")
#     f2.write(password)
# elif(userInput == "Read"):
#     askUser = input("What account name?")
#     for i in range(len(new_lines)):
#         if new_lines[i] == askUser:
#             print(new_lines[i+1])

# f.close()
# f2.close()