---
title: PHP
---

# PHP
- **Info**:
To summarize a Wikipedia page using PHP, you can use the MediaWiki API to fetch the content and then extract a summary. Here's a simple example:

```php
<?php
function summarizeWikipediaPage($pageTitle) {
    $url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&explaintext&format=json&titles=" . urlencode($pageTitle);
    $response = file_get_contents($url);
    $data = json_decode($response, true);
    
    $page = array_shift($data['query']['pages']);
    return $page['extract'] ?? 'No summary available.';
}

$title = "PHP"; // Example page title
$summary = summarizeWikipediaPage($title);
echo $summary;
?>
```

This script fetches the introductory text of the specified Wikipedia page and outputs it as a summary.