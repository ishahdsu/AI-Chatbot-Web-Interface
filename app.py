from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
import google.generativeai as genai

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

GOOGLE_API_KEY = 'MY_GOOGLE_API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    session['conversation'] = []
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    conversation = session.get('conversation', [])
 
    conversation.append(f"You: {user_message}")

    conversation_input = "\n".join(conversation)
    
    response = model.generate_content(conversation_input)
    response.resolve()

    response_text = response.text
    if response_text.startswith("Bot: Bot:"):
        response_text = response_text.replace("Bot: Bot:", "Bot:", 1)
    
    conversation.append(f"Bot: {response_text}")
  
    session['conversation'] = conversation
    
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
