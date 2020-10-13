from flask import Flask, jsonify

app = Flask(__name__)

status = [
  {"status": "ok" }
]


@app.route('/ping')
def ping():
  return jsonify(status)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False, threaded=False)
