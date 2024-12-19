import sys
from document_parser import NotSupportedFormat, FlashCardParser

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

    print(content[:30])
    return 0


if __name__ == '__main__':
    print("Return "+str(main(len(sys.argv),sys.argv)))
