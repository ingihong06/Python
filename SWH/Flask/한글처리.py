from flask import Flask, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    data = {'name': 'SWH', 'age': 3, 'subject': '코딩'}   # 딕셔너리
    header = jsonify(data)  # Break point 찍은 후 디버깅
    return header    # JSON 형식으로 데이터를 전달

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")