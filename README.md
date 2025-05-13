# Sentiment-Analyzer-using-Gemini
Sentiment Analyzer using Gemini
# 🌈 Gemini Sentiment Analyzer – Understand Emotions with AI 🤖💬

Welcome to the Gemini Sentiment Analyzer – a smart, clean, and lightweight Flask web app that leverages Google’s Gemini 1.5 Flash model to detect the emotion behind your words. Whether you paste a paragraph or upload a CSV file of customer feedback, our app tells you instantly: Is it Positive, Negative, or Neutral?

---

## 🌟 Key Features

🔮 Powered by Gemini 1.5 Flash (Google Generative AI)  
📝 Analyze single text inputs or batch files (CSV/TXT)  
📊 Instant visualization of sentiment distribution  
📁 Download sentiment results as a CSV file  
🧪 Built using Flask and Pandas – lightweight and easy to modify

---

## 🎯 Use Cases

- Analyze customer reviews from a CSV file  
- Test your product messaging for tone  
- Run sentiment tests on tweets, posts, or surveys  
- Use as a starting point for emotion-aware applications

---

## ⚙️ How It Works

1. 🖊️ Enter text in the input box OR upload a CSV/TXT file with a “text” column  
2. 🧠 Gemini processes each text input and classifies its sentiment  
3. 📈 The app shows sentiment results and a pie chart of counts  
4. 💾 Click “Download” to export your results in CSV format

---

## 🛠️ Tech Stack

- Python 3.10+ 🐍  
- Flask (backend web framework) 🌶️  
- Google Generative AI (Gemini) API 🔮  
- Pandas for CSV/text processing 🧮  
- HTML + Jinja2 for frontend 🎨

---

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/gemini-sentiment-analyzer.git
cd gemini-sentiment-analyzer
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your Google Generative AI API key in app.py:

python
Copy
Edit
genai.configure(api_key="YOUR_API_KEY")
Run the app:

bash
Copy
Edit
python app.py
Open your browser and visit: http://127.0.0.1:5000 🚀

📂 Project Structure
csharp
Copy
Edit
gemini-sentiment-analyzer/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Web UI template
├── static/                # Optional static files
├── requirements.txt       # Python dependencies
└── README.md              # This file
🔒 Security Note
Do not expose your API key in public repos! Use environment variables or a secrets manager for production deployments.

🌱 Roadmap Ideas
Sentiment bar chart + time series trends

Multi-language support

Emoji-based sentiment summary

Add file export in Excel or JSON

User login + sentiment history

👨‍💻 Author
Built with 💙 by Vedanth
Have ideas or want to contribute? Feel free to fork or open an issue!

📄 License
MIT License – free for personal and commercial use. Just give credit. 🙌

css
Copy
Edit

Would you like me to create a stylish HTML landing page or a PDF version of this README?







