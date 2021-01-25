#các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
import regex as re


#các hàm cần thiết

#hàm đọc nôi dung trang web
#kết quả trả về là 1 văn bản dạng chuỗi
def doc_noi_dung(url):
    raw_page = requests.get(url)
    content = BeautifulSoup(raw_page.text, "html.parser")
    return content

#hàm lấy các đường link web trong các nội dung đọc về
#kết quả trả về là một list chứa các link
def lay_duong_link(content):
    a_tag = content.find_all("a")
    result = []
    for item in a_tag:
        link = item.get('href')
        result.append(link)
    return result

#hàm kiểm tra tính hợp lệ của 1 đường link
def kiem_tra_link(link):
    result = []
    for i in link.find_all('href'):
        check = i.find('htts')
        if check is not None:
            result.append(check)
    return 

def chinh_sua_link(url, item):
    href = str(url) + item
    return
