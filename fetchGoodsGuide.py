#from bs4.element import Script
import requests
from bs4 import BeautifulSoup
import json
import re

#发送请求获取疫情数据的首页
home_page = requests.get('http://ncov.dxy.cn/ncovh5/view/pneumonia')
#变为utf8的编码
page  = home_page.content.decode()
print("-------------------------")
print(page)
print("-------------------------")

#找到里面的数据的标签
#创建解析对象
soup = BeautifulSoup(page,"lxml")
script = soup.find(id="fetchGoodsGuide")
script_data= script.string
#利用正则提取数据，是json字符串
json_str = re.findall(r'(\[.+\])',script_data)[0]
#将json字符串转为python数据
py_data = json.loads(json_str)
print(py_data)
# #将python数据保存到文件
with open('./public/data/fetchGoodsGuide.json','w',encoding='utf8') as fp:
    json.dump(py_data,fp,ensure_ascii=False)