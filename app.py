# # from flask import Flask, render_template, request, send_file
# # import google.generativeai as genai
# # import pandas as pd
# # import os
# # from io import BytesIO

# # app = Flask(__name__)
# # genai.configure(api_key="AIzaSyA3EWY3hgNSeZVoRAs30UH1DbSg7F2MLoE")

# # model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# # def analyze_sentiment(text):
# #     prompt = f"""
# #     Analyze the sentiment of the following text and respond with one of the following:
# #     - Positive
# #     - Negative
# #     - Neutral

# #     Text: "{text}"
# #     Sentiment:"""
# #     try:
# #         response = model.generate_content(prompt)
# #         return response.text.strip()
# #     except Exception as e:
# #         return f"Error: {str(e)}"

# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     sentiment = None
# #     text_input = None
# #     results_df = None
# #     download_link = None

# #     if request.method == 'POST':
# #         text_input = request.form.get('text')
# #         file = request.files.get('file')

# #         if file:
# #             filename = file.filename

# #             # 📄 Handle .txt file
# #             if filename.endswith('.txt'):
# #                 text_input = file.read().decode('utf-8')
# #                 sentiment = analyze_sentiment(text_input)

# #             # 📊 Handle .csv file
# #             elif filename.endswith('.csv'):
# #                 df = pd.read_csv(file)
# #                 if 'text' not in df.columns:
# #                     sentiment = "CSV must have a column named 'text'."
# #                 else:
# #                     df['sentiment'] = df['text'].apply(analyze_sentiment)
# #                     results_df = df

# #                     # Save to in-memory CSV for download
# #                     output = BytesIO()
# #                     df.to_csv(output, index=False)
# #                     output.seek(0)
# #                     return send_file(output, mimetype='text/csv', as_attachment=True, download_name='sentiment_results.csv')

# #         elif text_input:
# #             sentiment = analyze_sentiment(text_input)

# #     return render_template('index.html', sentiment=sentiment, text=text_input)

# # if __name__ == '__main__':
# #     app.run(debug=True)
# from flask import Flask, render_template, request
# import os
# import google.generativeai as genai
# import pandas as pd

# app = Flask(__name__)

# # Set your Gemini API key here
# genai.configure(api_key="AIzaSyA3EWY3hgNSeZVoRAs30UH1DbSg7F2MLoE")

# model = genai.GenerativeModel("models/gemini-1.5-flash")

# def analyze_sentiment(text):
#     prompt = f"What is the sentiment of the following text?\n\n\"{text}\"\n\nReply with only one word: Positive, Negative, or Neutral."
#     try:
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         return f"Error: {str(e)}"

# @app.route("/", methods=["GET", "POST"])
# def index():
#     sentiments = []
#     text = ""
    
#     if request.method == "POST":
#         text = request.form.get("text")
#         file = request.files.get("file")

#         # Handle direct text input
#         if text:
#             sentiment = analyze_sentiment(text)
#             sentiments.append({"text": text, "sentiment": sentiment})

#         # Handle file upload
#         elif file and file.filename.endswith((".csv", ".txt")):
#             df = None
#             if file.filename.endswith(".csv"):
#                 df = pd.read_csv(file)
#             else:
#                 # Assume one sentence per line for .txt files
#                 df = pd.DataFrame(file.read().decode("utf-8").splitlines(), columns=["text"])

#             for line in df["text"].dropna():
#                 sentiment = analyze_sentiment(line)
#                 sentiments.append({"text": line, "sentiment": sentiment})

#     return render_template("index.html", sentiments=sentiments, text=text)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, send_file
import os
import google.generativeai as genai
import pandas as pd
import io

app = Flask(__name__)

genai.configure(api_key="AIzaSyA3EWY3hgNSeZVoRAs30UH1DbSg7F2MLoE")
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Global variable to store last results
last_sentiments_df = pd.DataFrame()

def analyze_sentiment(text):
    prompt = f"What is the sentiment of the following text?\n\n\"{text}\"\n\nReply with only one word: Positive, Negative, or Neutral."
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    global last_sentiments_df
    sentiments = []
    text = ""
    
    if request.method == "POST":
        text = request.form.get("text")
        file = request.files.get("file")

        if text:
            sentiment = analyze_sentiment(text)
            sentiments.append({"text": text, "sentiment": sentiment})

        elif file and file.filename.endswith((".csv", ".txt")):
            df = None
            if file.filename.endswith(".csv"):
                df = pd.read_csv(file)
            else:
                df = pd.DataFrame(file.read().decode("utf-8").splitlines(), columns=["text"])

            for line in df["text"].dropna():
                sentiment = analyze_sentiment(line)
                sentiments.append({"text": line, "sentiment": sentiment})

        last_sentiments_df = pd.DataFrame(sentiments)

    # Sentiment count for chart
    sentiment_counts = last_sentiments_df["sentiment"].value_counts().to_dict() if not last_sentiments_df.empty else {}

    return render_template("index.html", sentiments=sentiments, text=text, sentiment_counts=sentiment_counts)

@app.route("/download")
def download_csv():
    global last_sentiments_df
    if last_sentiments_df.empty:
        return "No data to download."
    
    buffer = io.StringIO()
    last_sentiments_df.to_csv(buffer, index=False)
    buffer.seek(0)

    return send_file(
        io.BytesIO(buffer.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="sentiment_results.csv"
    )

if __name__ == "__main__":
    app.run(debug=True)
