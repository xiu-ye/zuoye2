from fractions import Fraction
from models import ExpressionNode


def evaluate(node):
    if node.is_leaf():
        return node.value.to_fraction()

    left = evaluate(node.left)
    right = evaluate(node.right)

    return {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }[node.op](left, right)


def is_valid(node):
    try:
        value = evaluate(node)
        if node.op == '/' and value.denominator == 1:
            return False
        return True
    except:
        return False