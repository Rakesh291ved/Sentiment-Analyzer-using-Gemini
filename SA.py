import google.generativeai as genai

# ✅ Configure with your actual Gemini 1.5 Flash API key
genai.configure(api_key="AIzaSyA3EWY3hgNSeZVoRAs30UH1DbSg7F2MLoE")

# ✅ Use the latest Gemini 1.5 Flash model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

def analyze_sentiment(text):
    prompt = f"""
    Analyze the sentiment of the following text. Respond with one of the following:
    - Positive
    - Negative
    - Neutral

    Text: "{text}"
    Sentiment:"""
    
    response = model.generate_content(prompt)
    return response.text.strip()

# 🔍 Test
text = "The service was absolutely fantastic and I loved every part of it."
sentiment = analyze_sentiment(text)
print("Sentiment:", sentiment)
