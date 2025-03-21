class ResultReporter:
    @staticmethod
    def generate_report(correct, wrong, output_file="Grade.txt"):
        """生成统计报告"""
        with open(output_file, 'w') as f:
            f.write(f"Correct: {len(correct)} ({', '.join(map(str, sorted(correct)))})\n")
            f.write(f"Wrong: {len(wrong)} ({', '.join(map(str, sorted(wrong)))})\n")

    @staticmethod
    def read_files(exercise_path, answer_path):
        """读取题目和答案文件"""
        with open(exercise_path) as f_ex, open(answer_path) as f_an:
            exercises = [line.strip() for line in f_ex if line.strip()]
            answers = [line.strip() for line in f_an if line.strip()]
        return exercises, answers