from flask import Flask, render_template, request, jsonify

app = Flask (__name__)

@app.route ('/')
def home():
    return render_template('hWorld.html')

@app.route ('/hello', methods=['POST'])
def hello():
    number = request.json['number']
    result = ["Hello World" for _ in range(number)]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)