
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
```

### 2. Install Required Libraries
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Set Up Your PDF File
Place your PDF file in the folder (e.g., `C:\Users\HP\Desktop\abstract_final` or any desired path) that you plan to use for processing.

### 4. Modify the Code
Update the path to your PDF in the code if needed. In the `main.py` file, modify the `pdf_path` variable:
```python
pdf_path = "path_to_your_pdf_file.pdf"
```

### 5. Run the Application
Execute the bot using the following command:
```bash
python main.py
```

The bot will load the PDF and allow you to query information based on its content.

## Structure of the Code
- **main.py**: The entry point where the bot processes the PDF and handles user queries.
- **pdf_loader.py**: Contains logic for loading and parsing PDF files.
- **tokenizer.py**: Handles the tokenization of the parsed content for further processing.
- **query_handler.py**: Manages user queries and generates responses using Huggingface models.

## Issues & Troubleshooting
- **Invalid PDF Path**: Ensure that the path to the PDF file is correct.
- **Model Loading Issues**: If you encounter errors related to model loading, ensure you have internet access to download the pretrained models.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- LangChain for PDF processing and chaining.
- Huggingface for the pretrained NLP models.
```

---

### **How to Add This README File**
1. In your project folder (`C:\Users\HP\Desktop\pdf bot`), create a file named `README.md`.
2. Copy the above content and paste it into the `README.md` file.
3. Save the file.

Once your `README.md` file is ready, you can proceed with pushing your code to GitHub, and the README will automatically be displayed on the repository page. #
