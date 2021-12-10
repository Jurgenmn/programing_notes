def sub(a, b):
    print(a - b)

sub(2, 3)

def multiply(a, b):
    print(a * b)
    return(a * b)


result = multiply(2, 3)
print(multiply(result, 3))

def div(a, b):
    return a / b

print(int(div(6, 2)))

def main():
    number1 = input ("Enter number 1: ")
    number2 = input("Enter number 2: ")
    print(int(number1) - int(number2))
    print(int(number1) * int(number2))
    print(int(number1) / int(number2))

main()
