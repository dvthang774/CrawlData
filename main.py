import folder_op,web_op

url_list = ['https://vietnamnet.vn/']
history = [] #chứa các đường link đã được duyệt
max_page = 1000 #quy định số lượng trang web được tải về
count = 0 #đếm số lượng trang web đã tải về
data_folder ="C:\\Users\\Admin\\crawlweb\\"

#kịch bản tải các trang web

while (count<max_page) and  (len(url_list)>0):
    url = url_list.pop(0)
    page = web_op.doc_noi_dung(url)
    links = web_op.lay_duong_link((page))
    for item in links:
        if web_op.kiem_tra_link(item):
            item = web_op.chinh_sua_link(url)
        if not ((item in url_list) and (item in history)):
            url_list.append(item)
    folder_op.luu_noi_dung(page, data_folder)
    history.append(url)
    count +=1

if __name__ == '__main__':
    start()