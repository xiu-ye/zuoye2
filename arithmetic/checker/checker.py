from .parser import ExpressionParser, AnswerParser
from .comparator import AnswerComparator
from .reporter import ResultReporter

def check_answers(ex_file, an_file):
    """整合检查流程"""
    correct = []
    wrong = []

    exercises, answers = ResultReporter.read_files(ex_file, an_file)

    for idx, (ex_line, an_line) in enumerate(zip(exercises, answers), start=1):
        try:
            ex_num, ex_content = ex_line.split('.', 1)
            expr_str = ex_content.split('=')[0].strip()
            py_expr = ExpressionParser.parse_problem(expr_str)

            an_num, an_value = an_line.split('.', 1)
            user_ans = AnswerParser.parse(an_value)

            if ex_num != an_num:
                raise ValueError(f"题号不匹配: {ex_num} vs {an_num}")

            if AnswerComparator.compare(py_expr, user_ans):
                correct.append(idx)
            else:
                wrong.append(idx)

        except Exception as e:
            print(f"Error on problem {idx}: {str(e)}")
            wrong.append(idx)

    ResultReporter.generate_report(correct, wrong)