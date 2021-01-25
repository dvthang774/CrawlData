# các hàm cần thiết
import os

a = os.chdir("D:\\crawl")
n = len(os.listdir(a))
#các hàm

#hàm này tạo tên file tự động, bắt đầu bằng cụm file name tiếp theo là số các file kết thúc là *.html
def tao_ten_file_tu_dong(name):

    k ="Crawl"+ str(n+1) + ".txt"
    return k

#hàm lưu nội dung vào file ở  thư mục chỉ định
def luu_noi_dung(content, folder):
    with open(folder, 'w') as f:
        f.write(content)
        f.close()
