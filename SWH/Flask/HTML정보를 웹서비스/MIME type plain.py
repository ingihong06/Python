from flask import Flask, Response
app = Flask(__name__)
@app.route("/")
def hello():
    data = '<html><head><title>SWH Sample</title></head><body><h1>HTML 입니다.</h1></body></html>'
    header = Response(data, status=200, mimetype='text/plain')
    return header    # 일반 텍스트 형식으로 데이터를 전달

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")