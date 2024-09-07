from src.core import document_processor, llm_integration

def run_cli():
    print("Welcome to Scriptorium!")
    
    content = input("Enter your markdown content: ")
    
    frontmatter, main_content = document_processor.process_document(content)
    
    print("\nExtracted frontmatter:")
    print(frontmatter)
    
    print("\nMain content:")
    print(main_content)
    
    summary = document_processor.summarize_content(main_content)
    print("\nSummary:")
    print(summary)
    
    prompt = "Summarize the following content: " + main_content
    llm_response = llm_integration.generate_response(prompt)
    
    print("\nLLM Response:")
    print(llm_response)