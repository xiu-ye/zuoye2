from cli import parse_args
from generator import generate_expression
from evaluator import evaluate
from utils import canonical_form
from models import Number
from utils import format_expression

def main():
    args = parse_args()

    if args.e and args.a:
        check_answers(args.e, args.a)
    else:
        generate_problems(args.n, args.r)

def generate_problems(n, r):
    generated = set()
    exercises = []
    answers = []

    while len(exercises) < n:
        expr = generate_expression(3, r)
        if not expr:
            continue

        cf = canonical_form(expr)
        if cf not in generated:
            generated.add(cf)
            exercises.append(expr)
            answers.append(evaluate(expr))

    save_exercises(exercises)
    save_answers(answers)


def check_answers(ex_file, an_file):
    """整合检查流程"""
    from checker.parser import ExpressionParser, AnswerParser
    from checker.comparator import AnswerComparator
    from checker.reporter import ResultReporter

    correct = []
    wrong = []

    # 读取文件
    exercises, answers = ResultReporter.read_files(ex_file, an_file)

    # 逐题检查
    for idx, (ex_line, an_line) in enumerate(zip(exercises, answers), start=1):
        try:
            # 解析题目
            ex_num, ex_content = ex_line.split('.', 1)
            expr_str = ex_content.split('=')[0].strip()
            py_expr = ExpressionParser.parse_problem(expr_str)

            # 解析答案
            an_num, an_value = an_line.split('.', 1)
            user_ans = AnswerParser.parse(an_value)

            # 验证题号
            if ex_num != an_num:
                raise ValueError(f"题号不匹配: {ex_num} vs {an_num}")

            # 比较答案
            if AnswerComparator.compare(py_expr, user_ans):
                correct.append(idx)
            else:
                wrong.append(idx)

        except Exception as e:
            print(f"处理第{idx}题时发生错误: {str(e)}")
            wrong.append(idx)

    ResultReporter.generate_report(correct, wrong)

def save_exercises(exercises):
    with open("Exercises.txt", "w") as f:
        for i, expr in enumerate(exercises, 1):
            f.write(f"{i}. {format_expression(expr)} =\n")


def save_answers(answers):
    with open("Answers.txt", "w") as f:
        for i, ans in enumerate(answers, 1):
            num = Number(ans.numerator)
            num.den = ans.denominator
            f.write(f"{i}. {num}\n")


if __name__ == "__main__":
    main()