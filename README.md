

# Sentiment Analysis API with LLM Integration  

This project implements a Sentiment Analysis API that processes user-uploaded CSV or XLSX files containing customer reviews. The API utilizes Groq's Large Language Models (LLM) to analyze the sentiment of the reviews and returns structured sentiment scores.  

## Table of Contents  

- [1. Approach to Solving the Problem](#1-approach-to-solving-the-problem)  
  - [1.1 API Design Using Flask](#11-api-design-using-flask)  
  - [1.2 File Handling and Data Extraction](#12-file-handling-and-data-extraction)  
  - [1.3 Integration with Groq API](#13-integration-with-groq-api)  
  - [1.4 Custom Sentiment Analysis](#14-custom-sentiment-analysis)  
  - [1.5 Aggregating Sentiment Scores](#15-aggregating-sentiment-scores)  
- [2. Implementation of Structured Response](#2-implementation-of-structured-response)  
- [3. Examples of API Usage with Sample Inputs/Outputs](#3-examples-of-api-usage-with-sample-inputsoutputs)  
- [4. Analysis of Results](#4-analysis-of-results)  
  - [4.1 Accuracy and Limitations](#41-accuracy-and-limitations)  
  - [4.2 Possible Improvements](#42-possible-improvements)  
- [5. Contributing](#6-contributing)  
- [6. License](#7-license)  

## 1. Approach to Solving the Problem  

The task required building a Sentiment Analysis API that processes user-uploaded CSV or XLSX files containing customer reviews. The reviews needed to be analyzed using Groq's Large Language Models (LLM), and the API would return a structured sentiment analysis, indicating the overall positive, negative, and neutral sentiment scores for the given reviews.  

### 1.1 API Design Using Flask  

I chose Flask for its simplicity and efficiency in creating APIs. Flask makes it easy to handle HTTP requests, file uploads, and data processing. The API consists of a single endpoint `/analyze_sentiment`, which accepts POST requests containing a CSV or XLSX file with customer reviews.  

### 1.2 File Handling and Data Extraction  

To handle file uploads, the Flask `request.files` functionality was used. This allowed users to upload files in CSV or XLSX format. `pandas` was used to read and process the file contents.  
- For CSV files, `pandas.read_csv()` was used to load the data.  
- For XLSX files, `pandas.read_excel()` was utilized.  

The reviews were then extracted from a specific column, assuming the column name was 'review'. The list of reviews was passed for further sentiment analysis.  

### 1.3 Integration with Groq API  

I integrated Groq’s LLM using the Groq client. This allowed the model to process each review. Each review was passed as a user message to the model, and the model's response was expected to provide a relevant sentiment for the given input. I created a new API key using Groq.  

The Groq API’s LLM model, "llama3-8b-8192", was selected to ensure powerful text generation with a balance of size and accuracy. The temperature was set to 0.5 to maintain coherent, but not overly creative, outputs. This level ensures a good trade-off between deterministic responses and diversity.  

### 1.4 Custom Sentiment Analysis  

After receiving the response from Groq’s LLM, I wrote a custom function called `analyze_response` that performed basic sentiment analysis. The response text was parsed and checked against predefined keywords for positive, negative, and neutral sentiments.  

**Keyword-Based Sentiment Detection:**  
- Positive keywords included words like "great", "excellent", "love", etc.  
- Negative keywords included words like "bad", "terrible", "disappointed", etc.  
- Neutral keywords consisted of words like "okay", "average", "fine", etc.  

The function calculated the occurrence of each type of keyword in the model’s response and provided a sentiment score based on the distribution of these keywords.  

### 1.5 Aggregating Sentiment Scores  

Once the individual reviews were processed, the API computed the overall sentiment by calculating the average sentiment scores for positive, negative, and neutral sentiments across all reviews. These scores were then structured into a JSON response.  

## 2. Implementation of Structured Response  

To maintain a clear and structured output, the response from the API was returned in JSON format. This format is widely used and makes it easy for users to interpret the results. The structured response helps users quickly understand the overall sentiment of the customer reviews without needing to delve into the details of individual reviews.  

**Response:**  
Upon successfully processing the uploaded file and analyzing the sentiment of the reviews, the API returns a JSON object which can be checked using Postman.  

Postman is a popular API testing tool that allows users to send requests to APIs and view responses in a user-friendly manner. It provides a graphical interface for creating HTTP requests and inspecting responses, making it ideal for testing and debugging.  

In this format:  
- `positive` represents the percentage of positive sentiment detected.  
- `negative` represents the percentage of negative sentiment detected.  
- `neutral` represents the percentage of neutral sentiment detected.  

The response was designed this way to give an overall sentiment trend rather than a detailed analysis of individual reviews. This makes it easier to understand the aggregate sentiment from a larger dataset of reviews.  

## 3. Examples of API Usage with Sample Inputs/Outputs  

### API Endpoint: `/analyze_sentiment`  

This endpoint accepts a POST request containing a CSV or XLSX file with customer reviews.  

**Sample Input:**  
Imagine a file named `reviews.csv` with the following content:  

```csv  
review  
"I absolutely love this product!"  
"The delivery service was terrible."  
"The product is okay but could be better."

**Sample API Call:**
You can test this API using a tool like curl. Here's how to call the API using the command line:

bash
curl -X POST http://localhost:5000/analyze_sentiment -F "file=@reviews.csv"  
Sample Output:
The output will be a structured JSON response with aggregated sentiment scores:

json
{  
  "positive": 0.33,  
  "negative": 0.33,  
  "neutral": 0.33  
}  
This output indicates that the overall sentiment across the provided reviews is evenly distributed among positive, negative, and neutral sentiments.

4. Analysis of Results
4.1 Accuracy and Limitations:
Keyword Matching: The current implementation uses a simplistic keyword matching approach for sentiment analysis. While this approach works for basic sentiment detection, it may miss nuanced expressions of sentiment, such as sarcasm or mixed sentiments within a single review. For example, "I love the product but hate the delivery" would not be correctly handled as both positive and negative sentiment.

LLM Response Handling: The LLM from Groq provides a generated response to the review, which is then analyzed. However, further refinement is needed to parse more complex or creative model outputs effectively.

4.2 Possible Improvements:
Advanced Sentiment Models: Integrating a pre-trained sentiment analysis model, such as VADER or BERT, could significantly improve accuracy. These models consider context and have been trained specifically on sentiment analysis tasks.

Handling Longer Reviews: For long reviews with mixed sentiments, segmenting the review into smaller parts and analyzing each segment separately could lead to more accurate overall results.

Error Handling Enhancements: While the current implementation checks for file format issues, it could be extended to handle other errors, such as missing data, malformed content, or Groq API failures (e.g., network timeouts).
