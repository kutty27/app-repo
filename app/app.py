from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Assisted GitOps Pipeline Running Successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
