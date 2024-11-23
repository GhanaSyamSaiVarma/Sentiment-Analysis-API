from flask import Flask, request, jsonify
from pandas import read_csv, read_excel
import requests
from groq import Groq  

app = Flask(__name__)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    
    file = request.files['file']
    if file.filename.endswith('.csv'):
        df = read_csv(file)
    elif file.filename.endswith('.xlsx'):
        df = read_excel(file)
    else:
        return jsonify({"error": "Invalid file format. Please upload a CSV or XLSX file."})

    
    reviews = df['review'].tolist()

    # Groq API integration
    client = Groq(api_key='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')
    model = "llama3-8b-8192"  

    results = []
    for review in reviews:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": review}],
            temperature=0.5, 
            max_tokens=1024,
            top_p=1
        )

        # Log the response to check the actual structure
        print(response)  # This will help debug the structure of the response

        # Access the 'choices' from the response
        try:
            message_content = response.choices[0].message.content  # Accessing via object attributes, not subscripting
            sentiment = analyze_response(message_content)
        except AttributeError as e:
            return jsonify({"error": f"An error occurred: {str(e)}. Please check the response structure."})

        results.append(sentiment)

    # Calculating overall sentiment scores
    positive_score = sum(result['positive'] for result in results) / len(results)
    negative_score = sum(result['negative'] for result in results) / len(results)
    neutral_score = sum(result['neutral'] for result in results) / len(results)

    return jsonify({
        "positive": positive_score,
        "negative": negative_score,
        "neutral": neutral_score
    })

def analyze_response(text):
    positive_keywords = ["great", "excellent", "satisfied", "love", "happy"]
    negative_keywords = ["bad", "terrible", "awful", "disappointed", "sad"]
    neutral_keywords = ["average", "mediocre", "quite", "okay", "fine", "neutral"]

    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for word in text.split():
        if word in positive_keywords:
            positive_count += 1
        elif word in negative_keywords:
            negative_count += 1
        elif word in neutral_keywords:
            neutral_count += 1

    total_count = positive_count + negative_count + neutral_count

    if total_count == 0:
        return {"positive": 0, "negative": 0, "neutral": 1}  

    positive_score = positive_count / total_count
    negative_score = negative_count / total_count
    neutral_score = neutral_count / total_count

    return {
        "positive": positive_score,
        "negative": negative_score,
        "neutral": neutral_score
    }

if __name__ == '__main__':
    app.run(debug=True)
