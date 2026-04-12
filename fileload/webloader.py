from langchain_community.document_loaders import TextLoader, WebBaseLoader

path="D:/text/"
loader = WebBaseLoader(web_paths=[path])
documents = loader.load()

print(len(documents))
print(documents[0])