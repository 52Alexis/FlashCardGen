# FlashCardGen

## Goals

- Create a seamless and efficient flashcard generation process
- Ensure compatibility with PDF inputs for easy content extraction
- Provide a user-friendly interface for creating and managing flashcards

## Implementation approach

We will use Python as the programming language for this project. To extract content from PDFs, we will utilize the open-source library PyMuPDF. For the user interface, we will use the Flask framework to create a web application. The flashcard generation algorithm will be developed using natural language processing libraries such as NLTK or SpaCy. For flashcard organization and categorization, we will leverage the capabilities of SQLite for database management. Lastly, we will integrate the spaced repetition algorithm using the open-source library Anki Vector.

## File list
- main.py: Starts the program and controls the flow.
- pdf_extractor.py: Extracts content from a PDF file.
- flashcard_generator.py: Generates flashcards from extracted content.
- user_interface.py:

    - Uploads a PDF file.
    - Customizes flashcards.
    - Organizes flashcards.

- database_manager.py:

    - Creates a database.
    - Adds flashcards to the database.
    - Retrieves flashcards from the database.
- spaced_repetition.py: Schedules flashcards for review using spaced repetition.
