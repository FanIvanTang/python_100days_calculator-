from art import logo


def add(num1, num2):
    """
    take two numbers num1 and num2 and return the sum of these two numbers
    """

    return num1 + num2


def subtract(num1, num2):
    """
    take two numbers num1 and num2 and return the value of num1 subtract num2
    """

    return num1 - num2


def multiply(num1, num2):
    """
    take two numbers num1 and num2 and returen the the value num1 times num2
    """

    return num1 * num2


def divide(num1, num2):
    """
    take two numbrs num1 and num2 and returen the value num2 is divided by num2, and num2 cannot be zero
    """

    return num1 / num2


def calculator():

    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    # print(operations)

    n1 = float(input("what is the first number?: "))

    for symbol in operations:
        print(symbol)

    is_continue = True

    while is_continue:

        operation_symbol = input("Pick an operation from the line above: ")
        n2 = int(input("what is the next number?: "))
        operation_function = operations[operation_symbol]

        answer = operation_function(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        n1 = answer

        is_continue = (
            input(
                f"Type 'y' to continue caluclation with {n1}, otherwise start a new caluclation: "
            ).lower()
            == "y"
        )

        if not is_continue:
            calculator()


if __name__ == "__main__":

    print(logo)

    # operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    # # print(operations)

    # n1 = int(input("what is the first number?: "))

    # for symbol in operations:
    #     print(symbol)

    # is_continue = True

    # while is_continue:

    #     operation_symbol = input("Pick an operation from the line above: ")
    #     n2 = int(input("what is the next number?: "))
    #     operation_function = operations[operation_symbol]

    #     answer = operation_function(n1, n2)

    #     print(f"{n1} {operation_symbol} {n2} = {answer}")

    #     n1 = answer

    #     is_continue = (
    #         input(
    #             f"Type 'y' to continue caluclation with {n1}, otherwise exit: "
    #         ).lower()
    #         == "y"
    #     )

    calculator()
