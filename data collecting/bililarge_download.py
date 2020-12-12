from bs4 import BeautifulSoup
import csv
import urllib.request
import requests
import os
# create class folders
os.makedirs('./queimage1/', exist_ok=True)
os.makedirs('./queimage2/', exist_ok=True)
os.makedirs('./queimage3/', exist_ok=True)
os.makedirs('./queimage4/', exist_ok=True)
os.makedirs('./queimage5/', exist_ok=True)
os.makedirs('./queimage6/', exist_ok=True)
os.makedirs('./queimage7/', exist_ok=True)

img_urls = []

csv_file = open('bili_1208new.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['img_id', 'cover_img_link', 'num_hit', 'class_name'])

# with open('numhit.html', 'rb') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

with open('moban.html', 'rb') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
i = 21000
for vd_lists in soup.find_all('ul', class_='vd-list mod-1'):
    for video_li in vd_lists.find_all('li', recursive=True):
        # print(video_li)
        # print("vd-list")
        # print(video_li)
    # for video_item in video_list.find_all('li', class_='l-item'):
        # print(video_item)
        try:
        ## find img_link===================================
            divl = video_li.find('div', class_='l')
            sp_module = divl.find('div', class_='spread-module')
            a_link = sp_module.a
            pic = a_link.find('div', class_='pic')
            lazy_img = pic.find('div', class_='lazy-img')
            img_link = lazy_img.img['src'][2:]
            img_link = img_link[:-15]
            img_link = "https://" + img_link
        #     #=================================================
        #     # find num_hits============================
            divr = video_li.find('div', class_='r')
            info_div = divr.find('div', class_='v-info')
            span_div = info_div.find('span', class_='v-info-i')
            span_tag = span_div.span
            print(span_tag)
            num_hits = span_tag.text
            # print("hh:", num_hits)
        #     span_tag = tags_div.find('span', class_='so-icon watch-num')
        #     # icon_tag = span_tag.find('i')
        #     num_hits = span_tag.text.split(' ')[8][:-2]
        #     # print(num_hits)
            if num_hits[-1] == "万":
                num_hits = float(num_hits[:-1]) * 10000
                num_hits = int(num_hits)
            else:
                num_hits = int(num_hits)
        #         # print(num_hits)
        #         # print(int(num_hits))
        #
        except Exception as e:
            img_link = None
        # set classes
    #filter
        # elif 100000 < num_hits <= 500000:
        #     class_num = 6

        if num_hits >= 500000:
            class_num = 7
        elif 100 < num_hits <= 1000:
            class_num = 2
        elif 1000 < num_hits <= 10000:
            class_num = 3
        elif 10000 < num_hits <= 50000:
            class_num = 4
        elif 50000 < num_hits <= 100000:
            class_num = 5
        elif 100000 < num_hits <= 500000:
            class_num = 6
        else:
            class_num = 1

        print(i, img_link, num_hits, class_num)
        # # print(i, num_hits)
        if img_link != "https://":
            img_urls.append([i, class_num, img_link])
        csv_writer.writerow([i, img_link, num_hits, class_num])
        i += 1
csv_file.close()


def request_download(IMAGE_URL, i, class_num):
    import requests
    r = requests.get(IMAGE_URL)
    with open('./queimage'+str(class_num)+'/'+str(i)+'.jpg', 'wb') as f:
        f.write(r.content)

# for f in imgs:
#     IMAGE_URL = f
#     request_download(IMAGE_URL, i)
#     print("downloading " + str(i) + "...")
#     i += 1
# def urllib_download(IMAGE_URL, num, class_num):
#     from urllib.request import urlretrieve
#     filename = './image'+str(class_num)+'/'+str(num)+'.jpg'
#     urlretrieve(IMAGE_URL, filename)


print(img_urls)
classsix_num = 0
download_errors = []
for f in img_urls:
    IMAGE_URL = f[2]
    i = f[0]
    class_num = f[1]
    try:
        classsix_num += 1
        request_download(IMAGE_URL, i, class_num)
        print("downloading " + str(i) + "...")
    except Exception as e:
        download_errors.append(i)

print("class six num:", classsix_num)
print("download errors::")
print(download_errors)