from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "안녕하세요"

@app.route("/<tag>")
def tag_hello(tag):
    return "<" + tag + ">Hello World<" + tag + ">"

@app.route("/<int:start>/<int:end>")
def age_hello(start, end):
    for b in range(start, end + 1):
        sum += b
    return str(sum)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")