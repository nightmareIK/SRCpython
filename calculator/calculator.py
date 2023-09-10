def sum(numbers):
    return  int(numbers[0]) + int(numbers[1])


def div(numbers):
    return  int(numbers[0]) / int(numbers[1])


def sub(numbers):
    return  int(numbers[0]) - int(numbers[1])


def mult(numbers):
    return  int(numbers[0]) * int(numbers[1])


numbers_input = input("Enter numbers separeted by space:  ").split(" ")
operation_input = input("Insert operator: (+ / - *) ")
result = 0

if len(numbers_input) != 2:
    print("Invalid Insert! Please insert 2 numbers! ")
else:
    if operation_input in "+/-*":
        if operation_input == "+":
            result = sum(numbers_input)

        elif operation_input == "/":
            result = div(numbers_input)

        elif operation_input == "-":
            result = sub(numbers_input)

        elif operation_input == "*":
            result = mult(numbers_input)

        print(f"Result is: {result}")

    else:
        print(f"Invalid Operator {operation_input}")
