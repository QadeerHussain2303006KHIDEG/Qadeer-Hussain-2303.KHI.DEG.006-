from flask import Flask
import requests

app = Flask(__name__)


@app.route("/add/<int:number_1>/<int:number_2>/")
def main(number_1: int, number_2: int):
    req='http://localhost:5000/add/{number_1}/{number_2}'
    response= requests.get(req)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
