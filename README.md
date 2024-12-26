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
| Feature                 | **Quizlet**                   | **Anki**                                | **Revisely**                     | **FlashCardGen** (Our Project)                 |
|-------------------------|-------------------------------|------------------------------------------|-----------------------------------|-----------------------------------------------|
| **Flashcard Creation**  | User creates flashcards manually. | Semi-automated with manual input options. | Semi-automated but requires edits. | Fully automated question and answer generation. |
| **PDF Integration**     | No integration.               | No integration.                          | Allows PDF import but limited. | Extracts and summarizes PDF information efficiently. |
| **Automation**          | Minimal (manual entry).       | Minimal (supports templates).            | Partial (PDF import and edits).   | End-to-end automated flashcard creation.      |
| **Question Generation** | Not available.                | Limited template-based options.          | Available but requires manual input. | Fully automated and tailored questions.       |
| **Ease of Use**         | Simple but time-consuming.    | Complex but powerful for advanced users. | Easy for semi-automated workflows. | Streamlined and efficient workflow.           |

# Implementation Approach
FlashCardGen is implemented in a Jupyter notebook. The notebook leverages open-source libraries and frameworks to:
- Extract important information from PDFs.
- Automatically generate questions and answers.

## File List
- **flashcardgen.ipynb**: The Jupyter notebook that contains all the code for extracting information from PDFs and generating flashcards.
- **example_input.pdf**: Sample input file.
- **flashcards.csv**: Sample output file.
- **parsing**: UI prototype to manage different file formats.

## How to run the code
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com//52Alexis/FlashCardGen.git
2. To use the predefined models for summarizing and generating flashcards, you need to create your Huggingface and Groqcloud API keys and paste them in the appropriate locations. (Code was tested on Google Colab, if running on local laptop maybe user have to modify the package installing commands in the notebook file.)
