import sys
from document_parser import NotSupportedFormat, FlashCardParser
from generator import FlashCardGenerator

def main(argc: int, argv: list):
    if argc < 2:
        print("insufficient arguments")
        return -1

    try:
        parser = FlashCardParser(argv[1])
        content = parser.parse()
    except NotSupportedFormat as e:
        print(e)
        return -2
    except FileNotFoundError as e:
        return -2

    #content ready to be used
    flashcards = FlashCardGenerator.generateFlashcard(content)
    output = ""
    for flashcard in flashcards:
        print(flashcard)
        output += flashcard
        output += "\n"

    output_file = open("flashcards.txt", "w")
    output_file.write(output)
    output_file.close()
    return 0


if __name__ == '__main__':
    print("Return "+str(main(len(sys.argv),sys.argv)))
