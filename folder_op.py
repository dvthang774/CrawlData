# các hàm cần thiết
import os

a = os.chdir('E:\\crawl')
n = len(os.listdir(a))
#các hàm

#hàm này tạo tên file tự động, bắt đầu bằng cụm file name tiếp theo là số các file kết thúc là *.html
def tao_ten_file_tu_dong(name):

    k ="Crawl"+ str(n+1) + ".html"
    return k

#hàm lưu nội dung vào file ở  thư mục chỉ định
def luu_noi_dung(content, folder):
    f = open("Crawl"+ str(n+1) + ".txt", 'w+', encoding='utf-8')
    f.write(str(content))
    f.close()
