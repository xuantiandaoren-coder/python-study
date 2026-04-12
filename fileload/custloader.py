from typing import Iterator, AsyncIterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document
from openai.types.beta.threads import file_path_annotation


class CustomLoader(BaseLoader):
    self.file_path = file_path_annotation

    def lazy_load(self) -> Iterator[Document]:
        with open(self.file_path, encoding="utf-8") as file:
            line_number = 0
            for line in file:
                line = line.strip()
                yield Document(page_content=line,
                               metadata = {"line_number":line_number,"length":len(line),"source":self.file_path})
                line_number += 1

    async def alazy_load(self) -> AsyncIterator[Document]:
        import aiofiles
        async with aiofiles.open(self.file_path, encoding="utf-8") as file:
            line_number = 0
            async for line in file:
                line = line.strip()
                yield Document(page_content=line,
                               metadata={"line_number": line_number, "length": len(line), "source": self.file_path})