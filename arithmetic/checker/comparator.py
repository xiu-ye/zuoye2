from fractions import Fraction

class AnswerComparator:
    @staticmethod
    def compare(problem_expr, user_answer):
        try:
            correct_ans = eval(problem_expr, {'Fraction': Fraction})
            return correct_ans == user_answer
        except:
            return False