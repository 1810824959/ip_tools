# author_li
# create time :2018/6/10
import requests
req=requests.get("http://127.0.0.1:5000/").text
print(req)