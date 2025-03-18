---
title: JavaScript
---

# JavaScript
- **Info**:
To summarize a Wikipedia page using JavaScript, you can use the MediaWiki API to fetch the content of the page and then extract a summary. Here's a concise example:

1. Use the Fetch API to get the page content.
2. Parse the JSON response.
3. Extract the summary from the "extract" field.

Here's a simple code snippet:

```javascript
async function summarizeWikipediaPage(title) {
    const response = await fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encodeURIComponent(title)}`);
    const data = await response.json();
    return data.extract; // This contains the summary
}

// Example usage
summarizeWikipediaPage('JavaScript').then(summary => console.log(summary));
```

This function fetches a summary of the specified Wikipedia page and logs it to the console.