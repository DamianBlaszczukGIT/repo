---
title: Java
---

# Java
- **Info**:
To summarize a Wikipedia page using Java, you can use libraries like Jsoup to fetch the content and then extract the relevant sections. Here's a simple example:

```java
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

public class WikipediaSummarizer {
    public static void main(String[] args) {
        try {
            String url = "https://en.wikipedia.org/wiki/Your_Page_Title"; // Replace with the desired Wikipedia page
            Document doc = Jsoup.connect(url).get();
            Element summary = doc.select("p").first(); // Get the first paragraph
            System.out.println(summary.text());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

This code fetches the specified Wikipedia page and prints the first paragraph, which often serves as a summary. Adjust the selector as needed to capture more content.