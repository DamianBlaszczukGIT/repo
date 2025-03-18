---
title: Python
---

# Python
- **Info**:
To summarize a Wikipedia page in Python, you can use the `wikipedia-api` library to fetch the content and then extract a summary. Here's a concise example:

```python
import wikipediaapi

def summarize_wikipedia_page(page_title):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(page_title)
    
    if page.exists():
        return page.summary
    else:
        return "Page not found."

# Example usage
summary = summarize_wikipedia_page("Python (programming language)")
print(summary)
```

This code retrieves the summary of the specified Wikipedia page. Make sure to install the `wikipedia-api` library using `pip install wikipedia-api` before running the code.