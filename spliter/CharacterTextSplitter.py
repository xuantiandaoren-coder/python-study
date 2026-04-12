
from langchain_text_splitters import CharacterTextSplitter

# 1. 初始化分割器
text_splitter = CharacterTextSplitter(
    separator="\n\n",    # 分隔符（只用一个）
    chunk_size=100,      # 每个块最多100个字符
    chunk_overlap=20,    # 块间重叠20个字符
    length_function=len, # 计算长度的函数
    keep_separator=False # 是否保留分隔符
)

# 2. 准备文本
long_text = """
第一段的内容。它包含一些文字。

第二段的内容。这个段落可能很长，会被切割。

第三段。内容很少。
"""

# 3. 执行切割
chunks = text_splitter.split_text(long_text)

# 4. 查看结果
for i, chunk in enumerate(chunks):
    print(f"--- 块 {i+1} (长度: {len(chunk)}) ---")
    print(chunk)
    print()