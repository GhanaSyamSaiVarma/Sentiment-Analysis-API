# Sentiment Analysis API with LLM Integration

## Overview
This project involves the development of a Sentiment Analysis API that processes customer reviews from user-uploaded CSV or XLSX files. The API leverages Groq's Large Language Models (LLM) to analyze the sentiment of the reviews and returns structured sentiment scores indicating the proportion of positive, negative, and neutral sentiments.

---

## Features
- **File Upload**: Accepts CSV and XLSX files containing customer reviews.
- **Sentiment Analysis**: Utilizes Groq's LLM to analyze each review and determine sentiment.
- **Structured Response**: Returns sentiment scores in a well-defined JSON format.
- **Error Handling**: Provides user feedback for unsupported file formats and other potential issues.

---

## Technologies Used
- **Flask**: Lightweight web framework for building the API.
- **Pandas**: Library for reading and processing CSV and XLSX files.
- **Groq API**: Integrates the LLM for sentiment analysis.

---

## API Endpoint
### `/analyze_sentiment`
- **Method**: POST
- **Description**: Accepts a file upload containing customer reviews and returns sentiment analysis results.

---

## Request Format
- **Content-Type**: `multipart/form-data`
- **File**: A CSV or XLSX file with a column named `review`.

### Sample Input
Example of a CSV file (`reviews.csv`):

| review                                 |
|----------------------------------------|
| "I absolutely love this product!"     |
| "The delivery service was terrible."  |
| "The product is okay but could be better." |

---

## Sample API Call
You can test the API using `curl`:

```bash
curl -X POST http://localhost:5000/analyze_sentiment -F "file=@reviews.csv"
```

---

## Sample Output
The API will return a JSON response with aggregated sentiment scores:

```json
{
  "positive": 0.33,
  "negative": 0.33,
  "neutral": 0.33
}
```

---

## Implementation Details
- **API Design**: Built using Flask for simplicity and efficiency.
- **File Handling**: Utilizes Pandas to read CSV and XLSX files.
- **Integration with Groq API**: Sends each review to Groq's LLM for sentiment analysis.
- **Custom Sentiment Analysis**: Implements a keyword-based approach to interpret sentiment from the LLM's response.
- **Aggregation of Results**: Computes overall sentiment scores from individual review analyses.

---

## Error Handling
The API includes basic error handling to manage unsupported file formats and other potential issues. For example, if an unsupported file format is uploaded, the API responds with:

```json
{
  "error": "Invalid file format. Please upload a CSV or XLSX file."
}
```

---

## Limitations and Future Improvements
1. **Keyword Matching**: The current implementation may not capture nuanced sentiments (e.g., sarcasm).
2. **LLM Response Handling**: Further refinement is needed to effectively parse complex responses.
3. **Advanced Models**: Future work could integrate more sophisticated sentiment analysis models like VADER or BERT.
4. **Error Handling Enhancements**: Additional checks for data integrity and API failures could improve robustness.

---

## Running the API
To run the API locally:

1. Ensure you have Python and the required libraries installed.
2. Save the provided Python code into a file named `app.py`.
3. Run the application:

   ```bash
   python app.py
   ```

4. Access the API at `http://localhost:5000/analyze_sentiment`.

---

## Conclusion
This Sentiment Analysis API provides a straightforward solution for analyzing customer reviews, leveraging advanced language models to derive meaningful insights from textual data. Future enhancements can further improve its accuracy and robustness.
