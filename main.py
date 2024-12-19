import sys
from document_parser import NotSupportedFormat, FlashCardParser
from generator import FlashCardGenerator, FlashCard

def main(argc: int, argv: list):
    if argc < 2:
        print("Error : No source file specified.")
        return -1
    outputfilename = "flashcards.txt"
    txtoutput = True
    if argc == 3:
        if str(argv[2]).split('.')[-1] != "csv" and str(argv[2]).split('.')[-1] != "txt":
            print("unsupported output format\nThe program will write the output to flashcards.txt")
        else :
            outputfilename = str(argv[2])
            txtoutput = outputfilename.split('.')[-1] == "txt"
    elif argc == 2:
        print("he program will write the output to flashcards.txt")
    if argc > 3:
        print("Error : Too many arguments")
        return -1


    try:
        parser = FlashCardParser(argv[1])
        content: str = parser.parse()
    except NotSupportedFormat as e:
        print(e)
        return -2
    except FileNotFoundError as e:
        return -2

    #content ready to be used
    flashcards: list[FlashCard] = FlashCardGenerator.generateFlashcard(content)
    if txtoutput:
        output = ""
        for flashcard in flashcards:
            print(str(flashcard))
            output += str(flashcard)
            output += "\n"
    else:
        output = "Question,Answer\n"
        for flashcard in flashcards:
            output += flashcard.getquestion()+','+flashcard.getanswer()+"\n"

    output_file = open(outputfilename, "w")
    output_file.write(output)
    output_file.close()
    return 0


if __name__ == '__main__':
    print("Return "+str(main(len(sys.argv),sys.argv)))
