import requests
from bs4 import BeautifulSoup

# 크롤링 하고 싶은 사이트 URL
target_url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1'

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(target_url, headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')

for music in musics:
    rank_tag = ('td.number')
    title_tag = ('td.info > a.title.ellipsis')
    singer_tag = music('td.info > a.artist.ellipsis')

    rank_text = rank_tag.text
    title_text = title_tag.text
    singer_text = singer_tag.text

    print = {
        'rank' = rank_text,
        'title' = title_text,
        'singer' = singer_text,
        }

