from .parser import ExpressionParser, AnswerParser
from .comparator import AnswerComparator
from .reporter import ResultReporter
from .checker import check_answers  # 新增导入

__all__ = ['check_answers']