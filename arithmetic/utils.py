import random
from fractions import Fraction
from models import Number

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_number(max_num):
    if random.random() < 0.5:
        return Number(random.randint(0, max_num-1))
    else:
        den = random.randint(2, max_num)
        num = random.randint(1, den-1)
        return Number(Fraction(num, den))

def canonical_form(node):
    if node.is_leaf():
        return str(node.value)
    left = canonical_form(node.left)
    right = canonical_form(node.right)
    if node.op in ['+', '*']:
        parts = sorted([left, right])
        return f"({parts[0]}{node.op}{parts[1]})"
    return f"({left}{node.op}{right})"

def validate_operation(left, right, op, max_num):
    from evaluator import evaluate
    if op == '-':
        return evaluate(left) >= evaluate(right)
    if op == '/':
        denominator = evaluate(right)
        return denominator != 0 and evaluate(left) < denominator
    return True


def format_expression(node):
    """将表达式树转换为带空格和括号的字符串"""

    def _format(node, parent_precedence=0):
        if node.is_leaf():
            return str(node.value)

        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }

        left_str = _format(node.left, precedence[node.op])
        right_str = _format(node.right, precedence[node.op])

        current_precedence = precedence[node.op]
        need_parenthesis = current_precedence < parent_precedence

        if node.op == '/' and not node.right.is_leaf():
            right_str = f"({right_str})"

        result = f"{left_str} {node.op} {right_str}"
        return f"({result})" if need_parenthesis else result

    return _format(node)