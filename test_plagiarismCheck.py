# test_main.py
import unittest
import subprocess
import os


class TestPlagiarismCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 初始化测试文件
        test_cases = {
            'orig.txt': '今天是星期天，天气晴，今天晚上我要去看电影。',
            'copy1.txt': '今天是周天，天气晴朗，我晚上要去看电影。',
            'copy2.txt': '现在是礼拜日，天气不错，今晚打算看电影。',
            'copy3.txt': '明天是周一，天气多云，晚上准备看电视剧。'
        }

        for name, content in test_cases.items():
            with open(name, 'w', encoding='utf-8') as f:
                f.write(content)

    @classmethod
    def tearDownClass(cls):
        # 清理测试文件
        for name in ['orig.txt', 'copy1.txt', 'copy2.txt', 'copy3.txt', 'ans.txt']:
            if os.path.exists(name):
                os.remove(name)

    def test_case1(self):
        """同义词替换测试"""
        subprocess.run('python main.py orig.txt copy1.txt ans.txt', shell=True)
        with open('ans.txt') as f:
            self.assertGreater(float(f.read()), 0.6)

    def test_case2(self):
        """语义相似测试"""
        subprocess.run('python main.py orig.txt copy2.txt ans.txt', shell=True)
        with open('ans.txt') as f:
            self.assertGreater(float(f.read()), 0.4)

    def test_case3(self):
        """不同内容测试"""
        subprocess.run('python main.py orig.txt copy3.txt ans.txt', shell=True)
        with open('ans.txt') as f:
            self.assertLess(float(f.read()), 0.2)


if __name__ == '__main__':
    unittest.main()