import re

def evaluate(expression):
    """
    Evaluates a simple mathematical expression in the format 'number operator number'.

    Args:
        expression: A string containing the mathematical expression.

    Returns:
        The result of the expression as a float.

    Raises:
        TypeError: If the expression is not a string.
        ValueError: If the expression is malformed, contains invalid numbers,
                    or an unsupported operator.
    """
    if not isinstance(expression, str):
        raise TypeError("Expression must be a string")

    # Basic parsing for a simple expression like "x + y"
    parts = re.split(r'(\s*[+\-*/]\s*)', expression)
    if len(parts) != 3:
        raise ValueError("Expression must be in the format 'number operator number'")

    try:
        left = float(parts[0].strip())
        right = float(parts[2].strip())
    except ValueError:
        raise ValueError("Invalid number in expression")

    op = parts[1].strip()

    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '/':
        if right == 0:
            raise ValueError("Cannot divide by zero")
        return left / right
    else:
        raise ValueError(f"Unsupported operator: {op}")

if __name__ == '__main__':
    # Simple test cases
    assert evaluate("10 + 5") == 15
    assert evaluate("10 - 5") == 5
    assert evaluate("10 * 5") == 50
    assert evaluate("10 / 5") == 2

    # Test for non-string input
    try:
        evaluate(123)
    except TypeError as e:
        assert str(e) == "Expression must be a string"

    # Test for malformed expression (invalid number)
    try:
        evaluate("a + 5")
    except ValueError as e:
        assert str(e) == "Invalid number in expression"

    # Test for malformed expression (wrong format)
    try:
        evaluate("1 + 2 + 3")
    except ValueError as e:
        assert str(e) == "Expression must be in the format 'number operator number'"

    print("All tests passed!")
