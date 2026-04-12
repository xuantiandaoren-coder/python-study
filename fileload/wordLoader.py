from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader

path="D:/text/"
loader = Docx2txtLoader(filename=path+"金庸书籍.txt",encoding="utf-8")
documents = loader.load()

print(len(documents))

# 分页信息遍历
for i,doc in enumerate(documents):
    print(f"文档片段{i+1} 内容为:{doc}")