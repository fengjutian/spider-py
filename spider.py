# # 获取页面
# import requests
# from bs4 import BeautifulSoup

# link = "http://www.santostang.com"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# r = requests.get(link, headers= headers)
# #print(r.text)

# soup = BeautifulSoup(r.text, "html.parser")
# title = soup.find("h1", class_="post-title").a.text.strip()
# print(title)

# with open("title_test.txt", "a+") as f:
#     f.write(title)


# import requests

# r = requests.get("http://www.santostang.com/")
# print("文本编码：", r.encoding)
# print("响应状态码：", r.status_code)
# print("字节方式的响应体：", r.content)
# print("字符串方式的响应体：", r.text)


import requests
from bs4 import BeautifulSoup

def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }

    movie_list = []
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250? start=' + str(i*25)
        r = requests.get(link, headers= headers, timeout= 10)
        print(str(i + 1), "页面响应状态码：", r.status_code)
        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
        return movie_list
movies = get_movies()
print(movies)