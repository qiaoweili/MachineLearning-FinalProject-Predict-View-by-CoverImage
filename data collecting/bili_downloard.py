from bs4 import BeautifulSoup
import csv
import urllib.request
import requests
import os

os.makedirs('./image/', exist_ok=True)
img_urls = []

csv_file = open('bili_vlog_dl.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['img_id', 'cover_img_link', 'num_hit'])

# 打开本地html============================================================
# soup = BeautifulSoup(open('bili_simple.html'))
# UNICODE ERROR: gbx:
#   solution: open(file_name, 'rb') 加b

with open('bili_vlog.html', 'rb') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# import url=============
# source = requests.get('https://search.bilibili.com/all?keyword=vlog&from_source=nav_search&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.10').text
# source = requests.get('https://search.bilibili.com/all?keyword=money')
# soup = BeautifulSoup(source, 'lxml')


mixin_list = soup.find('div', class_='mixin-list')
i = 1
# for mixin_lists in soup.find_all('div', class_='mixin-list'):
for video_list in soup.find_all('ul', class_='video-list clearfix'):

    for video_item in video_list.find_all('li', class_='video-item matrix'):

        try:
            # find img_link===================================
            image_div = video_item.find('div', class_='img')
            lazy_img = image_div.find('div', class_='lazy-img')
            img_link = lazy_img.img['src'][2:]
            img_link = "https://" + img_link
            #=================================================
            # find num_hits============================
            info_div = video_item.find('div', class_='info')
            tags_div = info_div.find('div', class_='tags')
            span_tag = tags_div.find('span', class_='so-icon watch-num')
            # icon_tag = span_tag.find('i')
            num_hits = span_tag.text.split(' ')[8][:-2]
            # print(num_hits)
            if num_hits[-1] == "万":
                num_hits = float(num_hits[:-1]) * 10000
                num_hits = int(num_hits)
                # print(num_hits)
                # print(int(num_hits))

        except Exception as e:
            img_link = None

        print(i, img_link, num_hits)
        # print(i, num_hits)
        if img_link != None:
            img_urls.append([i, img_link])
        i += 1
        csv_writer.writerow([i, img_link, num_hits])
csv_file.close()



def urllib_download(IMAGE_URL,num):
    from urllib.request import urlretrieve
    filename = './image/'+str(num)+'.jpg'
    urlretrieve(IMAGE_URL, filename)

print(img_urls)
download_errors = []
for f in img_urls:
    IMAGE_URL = f[1]
    i = f[0]
    try:
        urllib_download(IMAGE_URL, i)
    except Exception as e:
        download_errors.append(i)
    print("downloading " + str(i) + "...")


