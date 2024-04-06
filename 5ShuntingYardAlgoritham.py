def shunting_yard(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    operator = []
    for ch in expression.split():
        if ch.isalpha():
            output.append(ch)
        elif ch == '(':
            operator.append(ch)
        elif ch == ')':
            while operator and operator[-1] != '(':
                output.append(operator.pop())
            operator.pop()  # Discard the '('
        elif ch in precedence:
            while (operator and precedence.get(operator[-1], 0) >= precedence[ch]):
                output.append(operator.pop())
            operator.append(ch)

    while operator:
        output.append(operator.pop())

    return ' '.join(output)

# Example usage:
infix_expression = "a + b * c - d / e ^ f"
postfix_expression = shunting_yard(infix_expression)
print("Postfix expression:", postfix_expression)