from flask import Flask, request
from service import alertHandler
app = Flask(__name__)

@app.route('/alerts', methods=["POST"])
def alert_handler():
    return alertHandler(request.json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
