import re

def process_document(content):
    """
    Basic document processing: extracts frontmatter and content.
    """
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if match:
        frontmatter = match.group(1)
        content = content[match.end():]
    else:
        frontmatter = ""
    
    return frontmatter, content

def summarize_content(content):
    """
    Placeholder for content summarization.
    """
    return f"Summary of content ({len(content)} characters long)"