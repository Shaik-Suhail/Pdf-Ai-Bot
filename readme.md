# PDF AI Bot

## Project Overview
The **PDF AI Bot** is a Python-based application that allows users to upload PDF documents and query the content of the PDF using natural language. The bot utilizes **Langchain**, **Huggingface models**, **Langchain's PyPDFLoader**, and a tokenizer for NLP processing.

## Objectives
- Ingest and parse PDF documents.
- Tokenize the content for efficient processing.
- Use pretrained models from Huggingface to generate relevant answers based on the content of the PDFs.

## Functional Requirements
- **PDF Ingestion**: The bot uses Langchain's `PyPDFLoader` to read and parse PDF content.
- **Tokenization**: The content extracted from PDFs is tokenized for efficient processing and querying.
- **Model Utilization**: Huggingface's pretrained models are used to generate answers based on the PDF content.

## Non-Functional Requirements
- **Error Handling**: The bot gracefully handles errors, such as "Unable to process the PDF," and provides meaningful feedback to the user.

## Technical Stack
- **Python**: The core programming language for development.
- **LangChain**: Library used for PDF processing and chaining tasks.
- **Huggingface Transformers**: Used to utilize the models for NLP tasks.
- **Tokenizer**: Converts text into tokens for further processing.

## Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/pdf-ai-bot.git
cd pdf-ai-bot
2. Install Required Libraries
Install the required Python libraries:

pip install -r requirements.txt
3. Set Up Your PDF File
Place your PDF file in the folder (e.g., C:\Users\HP\Desktop\abstract_final or any desired path) that you plan to use for processing.

4. Modify the Code
Update the path to your PDF in the code if needed. In the main.py file, modify the pdf_path variable:

pdf_path = "path_to_your_pdf_file.pdf"
5. Run the Application
Execute the bot using the following command:

python main.py
The bot will load the PDF and allow you to query information based on its content.

Sample Questions and Responses
Here are some example interactions with the PDF AI Bot:

Question 1: What is the main topic of this PDF?

Response 1:

The main topic of this document is "Artificial Intelligence and its Applications."
Question 2: Can you summarize the conclusion of this document?

Response 2:

The conclusion emphasizes the importance of AI in shaping the future of technology and its impact on various industries.
Question 3: What are the key findings mentioned in the report?

Response 3:

The key findings include:
1. AI can improve efficiency in manufacturing.
2. Machine learning models are transforming data analysis.
3. Ethical concerns must be addressed as AI becomes more prevalent.
Question 4: What are the recommendations given in the PDF?

Response 4:

The recommendations suggest investing in AI research and development, fostering collaboration between industry and academia, and addressing the ethical challenges associated with AI technology.
Structure of the Code
main.py: The entry point where the bot processes the PDF and handles user queries.
pdf_loader.py: Contains logic for loading and parsing PDF files.
tokenizer.py: Handles the tokenization of the parsed content for further processing.
query_handler.py: Manages user queries and generates responses using Huggingface models.
Issues & Troubleshooting
Invalid PDF Path: Ensure that the path to the PDF file is correct.
Model Loading Issues: If you encounter errors related to model loading, ensure you have internet access to download the pretrained models.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
LangChain for PDF processing and chaining.
Huggingface for the pretrained NLP models.

This updated `README.md` includes a section with **Sample Questions and Responses**, so users can get an idea of how to interact with the bot.





