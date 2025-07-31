from textblob import TextBlob

def check_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Example usage
user_input = input("Enter a sentence: ")
result = check_sentiment(user_input)
print("Sentiment:", result)