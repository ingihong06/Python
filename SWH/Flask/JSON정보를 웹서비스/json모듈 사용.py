from flask import Flask, json, Response

app = Flask(__name__)


@app.route("/")
def hello():
    data = {'name': 'SWH', 'age': 3, 'subject': 'Coding'}  # 딕셔너리
    js = json.dumps(data)
    header = Response(js, status=200, mimetype='application/json')  # 응답코드와 MIME type을 별도로 기술
    return header  # JSON 형식으로 데이터를 전달


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")