from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

devices = []

@app.route('/')
def index():
    return render_template('index.html', devices=devices)

@app.route('/add', methods=['POST'])
def add_device():
    data = request.json
    devices.append(data)
    return jsonify({"status": "ok", "devices": devices})

if __name__ == '__main__':
    app.run(debug=True)
