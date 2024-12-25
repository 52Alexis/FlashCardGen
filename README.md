# FlashCardGen

## Overview
FlashCardGen is a tool designed to help students and professionals efficiently study and review important content from PDF documents. By extracting relevant information from PDFs, it automatically generates clear and concise questions and answers, facilitating effective study sessions.

## Goals
- Efficiently extract and summarize important information from PDFs.
- Automatically generate questions and answers based on the extracted content for effective studying.

## Features
- **PDF Extraction**: Extracts key information from PDF documents, including text and relevant data.
- **Automatic Flashcard Generation**: Creates questions and answers based on the extracted content.

## Requirements
### P0:
- **PDF Extraction**: Extract important information from PDFs.
- **Flashcard Generation**: Generate clear and concise questions and answers based on the extracted information.

## Competitive Analysis
- **Flashcard App**: Limited PDF integration, lacks automatic question generation.
- **StudyToolX**: Offers PDF integration and question generation but lacks full automation.
- **FlashyCardsPro**: Lacks automatic PDF information extraction.

## Implementation Approach
FlashCardGen is implemented in a Jupyter notebook. The notebook leverages open-source libraries and frameworks to:
- Extract important information from PDFs.
- Automatically generate questions and answers.

## File List
- **flashcardgen.pynb**: The Jupyter notebook that contains all the code for extracting information from PDFs and generating flashcards.

## How to run the code
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com//52Alexis/FlashCardGen.git
2. To use the predefined models for summarizing and generating flashcards, you need to create your Huggingface and Groqcloud API keys and paste them in the appropriate locations. 
