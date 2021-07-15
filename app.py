from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['get'])
def get():
    return render_template('reqres.html')  




if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")