# FlashCardGen

## Goals

- Efficiently extract and summarize important information from PDFs
- Generate clear and concise questions and answers for effective studying
- Provide a user-friendly interface for seamless interaction

## Competitive Analysis
Flashcard App: A Limited PDF integration, lacks automatic question generation
StudyToolX: Offers PDF integration and question generation, but lacks user-friendly interface
FlashyCardsPro: User-friendly interface, but lacks automatic PDF information extraction

## Implementation approach

We will use Python as the programming language for this project. We will analyze the requirements to identify the difficult points and select appropriate open-source libraries and frameworks to efficiently extract and summarize important information from PDFs, generate clear and concise questions and answers, and provide a user-friendly interface for seamless interaction.

## File list
- main.py: Initiates the program execution.
- pdf_processor.py: Extracts information from the provided PDF file.
- flashcard_generator.py:
    - Generates flashcards from the extracted information.
    - Allows review of the generated flashcards.

- user_interface.py:
    - upload_pdf(pdf_path: str): Uploads the PDF file to be processed.
    - display_flashcards(flashcards: list): Displays the generated flashcards to the user.
