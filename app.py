from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get('https://catfact.ninja/fact')
        if response.status_code == 200:
            data = response.json()
            fact = data['fact']
        else:
            fact = "Could not fetch cat fact. Try again later."
    except Exception as e:
        fact = f"Error: {e}"

    return render_template_string('''
        <html>
        <head><title>Cat Fact</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>🐱 Random Cat Fact</h1>
            <p>{{ fact }}</p>
        </body>
        </html>
    ''', fact=fact)

if __name__ == '__main__':
    app.run(debug=True)
