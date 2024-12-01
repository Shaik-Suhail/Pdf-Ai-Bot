from pdf_loader import load_and_parse_pdf
from tokenizer import tokenize_and_embed
from query_handler import query_pdf

def main():
    pdf_path = "C:\\Users\\HP\\Desktop\\abstract_final.pdf"  # Replace with the path to your PDF
    parsed_docs = load_and_parse_pdf(pdf_path)
    
    if not parsed_docs:
        print("Unable to parse the PDF.")
        return
    
    tokens = tokenize_and_embed(parsed_docs)
    if not tokens:
        print("Tokenization failed.")
        return

    while True:
        query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == "exit":
            print("Exiting...")
            break
        
        results = query_pdf(parsed_docs, query)
        if results:
            for result in results:
                print(f"Result: {result.page_content}")
        else:
            print("No relevant information found.")

if __name__ == "__main__":
    main()
