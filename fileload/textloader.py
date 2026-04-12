from langchain_community.document_loaders import TextLoader

path="D:/text/"
loader = TextLoader(filename=path+"金庸书籍.txt",encoding="utf-8")
documents = loader.load()

print(len(documents))
print(documents[0])