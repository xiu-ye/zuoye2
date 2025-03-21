# main.py
import sys
import re
import jieba
from datasketch import MinHash, MinHashLSH


def preprocess_text(text):
    """文本预处理流水线"""
    # 全角转半角
    text = text.translate(str.maketrans('，。！？【】（）％＃＠＆“”‘’；：',
                                        ',.!?[]()%#@&""\';:'))
    # 去除特殊符号
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', ' ', text)
    # 精确模式分词
    words = jieba.lcut(text)
    # 过滤停用词（根据实际需要扩展）
    stop_words = {"的", "了", "在", "是", "我", "有", "和", "就"}
    return [word.lower() for word in words if word.strip() and word not in stop_words]


def calculate_similarity(orig_tokens, copy_tokens):
    """使用MinHash计算相似度"""
    # 创建MinHash对象
    m1 = MinHash(num_perm=128)
    m2 = MinHash(num_perm=128)

    # 生成哈希值
    for token in orig_tokens:
        m1.update(token.encode('utf8'))
    for token in copy_tokens:
        m2.update(token.encode('utf8'))

    # 计算Jaccard相似度
    return m1.jaccard(m2)


def main():
    # 命令行参数校验
    if len(sys.argv) != 4:
        print("Usage: python main.py <原文文件> <抄袭文件> <答案文件>")
        sys.exit(1)

    orig_path, copy_path, ans_path = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # 读取文件内容
        with open(orig_path, 'r', encoding='utf-8') as f:
            original = f.read()
        with open(copy_path, 'r', encoding='utf-8') as f:
            copy = f.read()
    except Exception as e:
        print(f"文件读取失败: {str(e)}")
        sys.exit(1)

    # 文本预处理
    orig_tokens = preprocess_text(original)
    copy_tokens = preprocess_text(copy)

    # 计算相似度
    similarity = calculate_similarity(orig_tokens, copy_tokens)

    # 结果写入
    try:
        with open(ans_path, 'w', encoding='utf-8') as f:
            f.write(f"{max(0.0, min(similarity, 1.0)):.2f}")
    except Exception as e:
        print(f"结果写入失败: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    # 禁用jieba的并行分词（确保线程安全）
    jieba.disable_parallel()
    main()