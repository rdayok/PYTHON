
def mathematical_operation(operand1, operation_operator, operand2):
    if operation_operator == "+":
        result = f"The sum of operands is: {operand1 + operand2}"
    elif operation_operator == "-":
        result = f"The difference of left operand to right operand is: {operand1 - operand2}"
    elif operation_operator == "*":
        result = f"The product of right operand and left operand is: {operand1 * operand2}"
    elif operation_operator == "**":
        result = f"The result of raising left operand to right operand is: {operand1 ** operand2}"
    elif operation_operator == "/":
        result = f"The division of left operand by right operand is: {operand1 / operand2}"
    elif operation_operator == "%":
        result = f"The mod of left operand by left operand is: {operand1 % operand2}"
    else: result = "Please supply and operator next time"

    return result


left_operand = int(input("Please enter your left operand: \t"))
right_operand = int(input("Please enter your right operand: \t"))
operator = input("Please enter you operator: \t")

print(mathematical_operation(left_operand, operator, right_operand))
