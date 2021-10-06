
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    news = []
    # 新建数组存放热搜榜
    hot_url = 'https://s.weibo.com/top/summary/'
    # 热搜榜链接
    r = requests.get(hot_url)

    r.encoding = 'utf-8'   #解析编码
    # 向链接发送get请求获得页面
    soup = BeautifulSoup(r.text, 'lxml')
    print(r.text)
    # 解析页面

    urls_titles = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')
    hotness = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > span')

    for i in range(len(urls_titles)-1):
        hot_news = {}
        # 将信息保存到字典中
        hot_news['title'] = urls_titles[i+1].get_text()
        # get_text()获得a标签的文本
        hot_news['url'] = "https://s.weibo.com"+urls_titles[i]['href']
        # ['href']获得a标签的链接，并补全前缀
        hot_news['hotness'] = hotness[i].get_text()
        # 获得热度文本
        news.append(hot_news)
        # 字典追加到数组中

    print(news)

    import datetime
    today = datetime.date.today()
    f = open('./1热搜榜-%s.doc'%(today), 'w', encoding='utf-8')
    for i in news:
        f.write(i['title'] + '    ,    ' + i['url'] + ','+ i['hotness'] + '\n')
