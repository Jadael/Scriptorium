import unittest
from src.core import document_processor, llm_integration

class TestCore(unittest.TestCase):
    def test_process_document(self):
        content = """---
title: Test Document
---
This is the main content."""
        frontmatter, main_content = document_processor.process_document(content)
        self.assertEqual(frontmatter, "title: Test Document")
        self.assertEqual(main_content, "This is the main content.")

    def test_summarize_content(self):
        content = "This is a test content."
        summary = document_processor.summarize_content(content)
        self.assertTrue(summary.startswith("Summary of content"))

    def test_generate_response(self):
        prompt = "Test prompt"
        response = llm_integration.generate_response(prompt)
        self.assertTrue(response.startswith("LLM response to:"))

if __name__ == "__main__":
    unittest.main()