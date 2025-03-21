import re
from fractions import Fraction


class ExpressionParser:
    @staticmethod
    def parse_problem(expr_str):
        """解析题目表达式为可计算表达式"""
        expr = expr_str.replace('×', '*').replace('÷', '/')
        expr = ExpressionParser._convert_mixed_numbers(expr)
        expr = ExpressionParser._convert_fractions(expr)
        return expr

    @staticmethod
    def _convert_mixed_numbers(expr):
        """处理带分数 2'3/4 → (2 * 4+3)/4"""
        return re.sub(
            r"(\d+)'(\d+)/(\d+)",
            lambda m: f"Fraction({int(m.group(1))}*{int(m.group(3))}+{int(m.group(2))}, {int(m.group(3))})",
            expr
        )

    @staticmethod
    def _convert_fractions(expr):
        """转换分数和整数"""
        expr = re.sub(r"(\d+)/(\d+)", r"Fraction(\1,\2)", expr)
        return re.sub(r"\b(\d+)\b", r"Fraction(\1)", expr)


class AnswerParser:
    @staticmethod
    def parse(answer_str):
        ans = answer_str.strip()
        if "'" in ans:
            return AnswerParser._parse_mixed_number(ans)
        elif '/' in ans:
            return AnswerParser._parse_fraction(ans)
        else:
            return Fraction(int(ans))

    @staticmethod
    def _parse_mixed_number(s):
        parts = s.split("'")
        whole = int(parts[0])
        num, den = map(int, parts[1].split('/'))
        return Fraction(whole * den + num, den)

    @staticmethod
    def _parse_fraction(s):
        num, den = map(int, s.split('/'))
        return Fraction(num, den)