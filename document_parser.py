from docx import Document
from pypdf import PdfReader

class NotSupportedFormat(Exception):
    def __init__(self, format:str):
        self.format = format

    def __str__(self):
        return f"File {self.format} not supported"


class FlashCardParser:
    def __init__(self,filename:str):
        self.__filename = filename

    def __pdfparser(self):
        # raise NotImplementedError("pdf parse is not yet implemented")
        text=""
        reader = PdfReader(self.__filename)
        for page in reader.pages:
            text+=page.extract_text().replace('\n','')
        return text.strip(' ')

    def __docxparser(self):
        doc = Document(self.__filename)
        text=""
        for paragraph in doc.paragraphs:
            text+=paragraph.text+' '
        return text.strip(' ')


    def __txtparser(self):
        file = open(self.__filename,"r")
        text = file.read()
        text.replace('\n','')
        file.close()
        return text.strip(' ')


    def parse(self):
        try:
            if str.endswith(self.__filename, '.txt'):
                content=self.__txtparser()
            elif str.endswith(self.__filename, '.pdf'):
                content=self.__pdfparser()
            elif str.endswith(self.__filename, '.docx'):
                content=self.__docxparser()
            else:
                raise(NotSupportedFormat('.'+self.__filename.split('.')[-1]))

            return content
        except FileNotFoundError as e:
            print(self.__filename +" was not found in the active directory")
            raise e


