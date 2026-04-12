from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 初始化分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,      # 每个块最多100个字符
    chunk_overlap=20,    # 块之间重叠20个字符
    length_function=len, # 使用内置的len函数计算长度（字符数）
    separators=["\n\n", "\n", "。", "！", "？", "；", "，", " ", ""]
    # 注意：这里添加了中文标点作为分隔符
)

# 2. 准备长文本
long_text = """
这是第一段。它包含多个句子。这是一个示例。

这是第二段。它用于演示递归分割的工作方式。
这个段落很长，可能会被进一步切分，因为它包含了很多内容。
"""

# 3. 执行切割
chunks = text_splitter.split_text(long_text)

# 4. 查看结果
for i, chunk in enumerate(chunks):
    print(f"--- 块 {i+1} (长度: {len(chunk)}) ---")
    print(chunk)
    print()