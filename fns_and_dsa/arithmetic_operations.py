def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.

    Parameters:
    - num1 (float): first number
    - num2 (float): second number
    - operation (str): 'add', 'subtract', 'multiply', 'divide'

    Returns:
    - float: result of the arithmetic operation
    - str: error message for invalid operations or division by zero
    """
    operation = operation.strip().lower()

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"

