# các hàm cần thiết
import os
import constant

if not os.path.exists(constant.EXPORT_ROOT_FOLDER):
    os.makedirs(constant.EXPORT_ROOT_FOLDER)

a = os.chdir(constant.EXPORT_ROOT_FOLDER)
n = len(os.listdir(a))
#các hàm

#hàm này tạo tên file tự động, bắt đầu bằng cụm file name tiếp theo là số các file kết thúc là *.html
def tao_ten_file_tu_dong(name):

    k ="Crawl"+ str(n+1) + ".html"
    return k

#hàm lưu nội dung vào file ở  thư mục chỉ định
def luu_noi_dung(content, folder, urlIndex):
    print("Saving data to file", "Crawl"+ str(urlIndex) + ".txt")
    f = open(folder+"/Crawl"+ str(urlIndex) + ".txt", 'w+', encoding='utf-8')
    f.write(str(content))
    f.close()

def create_directory(path) :
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
