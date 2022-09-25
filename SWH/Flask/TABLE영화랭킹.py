import requests
from bs4 import BeautifulSoup  # BeautifulSoup import
from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def movieRank():
    data = {}
    response = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다
    ranking = 1
    for tag in soup.select('div[class=tit3] a'):
        data[str(ranking) + '위'] = tag.text
        ranking = ranking + 1
    header = jsonify(data)  # Break point 찍은 후 디버깅
    return render_template('TABLE영화랭킹.html', datha = list(data.items()))  # JSON 형식으로 데이터를 전달

    # return render_template('TABLE영화랭킹.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")