import requests
from bs4 import BeautifulSoup  # BeautifulSoup import

response = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109ㄴ')
html = response.text
soup = BeautifulSoup(html, 'html.parser')  # html.parser를 사용해서 soup에 넣겠다
ranking = 1
for tag in soup.select('div[class=tit3] a'):
    print(str(ranking) + '위 : ' + tag.text)
    # print(tag)
    # url = tag.get('href')
    # print(url)
    ranking = ranking + 1
    #
    # requests.get('https://movie.naver.com' + url)