

class FlashCardGenerator:
    def generateFlashcard(self,source: str):
        tokens = self.generateTokens(source)

        flashcards = []
        return flashcards

    def generateTokens(self,data_to_tokenize):

        tokens = []
        return tokens

class FlashCard:
    def __init__(self,Q:str,A:str):
        self.__question=Q
        self.__answer=A

    def flfromlist(QA:list):
        return FlashCard(QA[0],QA[1])

    def flfromdict(QA:dict):
        return FlashCard(QA['Question'],QA['Answer'])

    def __str__(self):
        return "Question : "+self.__question+ "\n\tAnswer: "+self.__answer

    def todict(self):
        return {"Question":self.__question, "Answer":self.__answer}

    def tolist(self):
        return [self.__question, self.__answer]

    def setquestion(self,Q:str):
        self.__question=Q

    def setanswer(self,A:str):
        self.__answer=A

    def getquestion(self):
        return self.__question

    def getanswer(self):
        return self.__answer

