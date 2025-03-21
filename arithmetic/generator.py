import random
from models import ExpressionNode
from utils import generate_number, validate_operation


def generate_expression(max_ops, max_num, current_ops=0):
    if current_ops > max_ops:
        return None

    if random.random() < 0.3 or current_ops == max_ops:
        return ExpressionNode(value=generate_number(max_num))

    op = random.choice(['+', '-', '*', '/'])
    left = generate_expression(max_ops, max_num, current_ops + 1)
    right = generate_expression(max_ops, max_num, current_ops + 1)

    if not validate_operation(left, right, op, max_num):
        return generate_expression(max_ops, max_num, current_ops)

    return ExpressionNode(left=left, op=op, right=right)