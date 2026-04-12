import tiktoken
from langchain_text_splitters import TextSplitter, TokenTextSplitter

text = ""

text_splitter = TokenTextSplitter(
    encoding_name="cl100k_base",
    chunk_size = 30,
    chunk_overlap=5
)

enc = tiktoken.get_encoding("cl100k_base")

chunk = text_splitter.get_chunk(text)

for  i,chunk in enumerate(chunk):
    print(f"{i}: {chunk}")
    print(f"{i}: {len(enc.encode(chunk))}")