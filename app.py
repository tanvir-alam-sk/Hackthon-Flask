from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/render')
def render():
    return render_template('render.html')


@app.route('/api/send-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
