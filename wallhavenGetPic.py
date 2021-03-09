import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import io
from PIL import Image
import requests


def nsfw_img_download(req, cookies, header, dirname):
    lt = re.findall(r'<li><figure.*?>.*?<a class="preview" href="(.*?)" .*?></a>.*?</figure></li>', req, flags=re.S)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    download_src = 'https://w.wallhaven.cc/full/'
    for img_src in lt:
        img_src = download_src + img_src[-6:-4] + '/wallhaven-' + img_src[-6:] + '.jpg'
        file_name = dirname + '/' + img_src[-10:]
        try:
            response = requests.get(img_src, cookies=cookies, headers=header).content
            print(f'开始下载{file_name}')
            with open(file_name, 'wb') as f:
                f.write(response)
            print("下载完成")

        except urllib.error.HTTPError as e:
            print(e)


def img_download(req, cookies, header, dirname):
    lt = re.findall(r'<li><figure.*?>.*?<a class="preview" href="(.*?)" .*?></a>.*?</figure></li>', req, flags=re.S)
    #r'<li><figure.*?>.*?<a class="preview" href="(.*?)" .*?></a>.*?</figure></li>'
    lt1 = re.findall(r'<span class="wall-res">(.*?)</span>', req, flags=re.S)

    if not os.path.exists(dirname):
        os.mkdir(dirname)
    download_src = 'https://w.wallhaven.cc/full/'
    for img_src in lt:
        img_src = download_src + img_src[-6:-4] + '/wallhaven-' + img_src[-6:] + '.jpg'
        file_name = dirname + '/' + img_src[-10:]
        # request = urllib.request.Request(,header)

        try:
            response = requests.get(img_src, cookies=cookies, headers=header).content
            print(f'开始下载{file_name}')
            with open(file_name, 'wb') as f:
                f.write(response)
            print("下载完成")

        except urllib.error.HTTPError as e:
            print(e)


# def request_get(url,cookies,headers,page):
#     page_url = url+str(page)
#     request = requests.get(url=page_url,cookies=cookies,headers=headers)
#     request.encoding = 'utf-8'
#     return request.text

def main(url,type, dirname):
    print("开始下载")
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    cookies = {
        '_pk_id.1.01b8': '08902011301c5c15.1606458567.',
        '_pk_ses.1.01b8': '1',
        '__cfduid':'d50daa07ee1528f9dbaf48044acb2f1201609995853',
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d':'eyJpdiI6Im56QXBEWTFLOHdwS0tTV1pcL1wvMVl2Zz09IiwidmFsdWUiOiIrbzlhWFN1RXJwSzVKOWlIN2RDblFZTlwvRllLNmtLdFFtWmZuOGMxd1ZaclBZMUM0S2p6dkxtS096UmRyNUFldHpTd25SWmQrZzQxVVJsWllwM0dOdGM1c2pvaHpiVDlWVXJYd0sxWm5tcVdXQ2VhdXNlcHQ5RHFMQld5ZzNnSEJndHUzZlZwdlpxcEVWZ3VjSkVobzdhYzV3eWtHZFUwOUlcL0trcndsNng2ZG1NM1wvanNScUlWNlAwUDl5NGU5RzciLCJtYWMiOiJkODc5ZjZjZmNjZTA2NzQzNzcxN2Y1YjkxMjdiNGQyMjc4Zjg0NzY3NTRmNTkwN2Q3ZTkwYTE3MmIxYzU3ZWU4In0%3D',
        'wallhaven_session':'eyJpdiI6IlYyeTgxYXFXMUsxdlZCbUVHVmh2YUE9PSIsInZhbHVlIjoiTjlNelBCMFNZNHZZM2ZibE1BZ2d0NUdsYzlcL3dGXC9uZ3BHbEZkdmpxVE1iZ1ZkMUlqOFR0ZGZCcDVTRHdBeExPIiwibWFjIjoiNDczNDEyYjM3MDcwMmNlYjdiYjFmZWY4MjQ1MzMwY2U1ODEyNWYwOWQ4MjYxOWU3OTZlZGE1NTExMTcwOTdiYSJ9',
        'XSRF-TOKEN':'eyJpdiI6IkpCeHRBM0ZFa0RYenpxcFRVOU44XC9RPT0iLCJ2YWx1ZSI6IldDallUbFwvbXlnZitRQlgrNkRUOXhhMTcycWtUcGpZNjcxMDJ3YTlJUlo2SnZiVkQ4QzFCeGxyTlo2VnZwWTMyIiwibWFjIjoiYTcxNzljZDA5NGRkOGI2NDgwMzg0MjczZWRmY2RiODA3N2EzNTdiN2RmMTc4ZmU4NzNmMDk1NGMwYzg4NGUwZiJ9'
    }
    if type == 'normal':
        # page_start = int(input("input start pages:"))
        # page_end = int(input("input end pages:"))
        for page in range(24, 100):
            print(f"开始传输第{page}页数据")
            page_url = url + str(page)
            request = requests.get(page_url, cookies=cookies, headers=headers).text
            img_download(request, cookies, headers, dirname)
            print(f'第{page}传输完成')
            print()
            print()
            time.sleep(0.2)
    else:
        for page in range(94,101):
            print(f"nsfw 开始传输第{page}页数据")
            page_url = url + str(page)
            request = requests.get(page_url, cookies=cookies, headers=headers).text
            nsfw_img_download(request, cookies, headers, dirname)
            print(f'第{page}传输完成')
            print()
            print()
            time.sleep(0.2)


if __name__ == "__main__":
    dirname = 'wallhaven'
    url = 'https://wallhaven.cc/search?categories=111&purity=100&atleast=1920x1080&topRange=1M&sorting=favorites&order=desc&page='
    main(url,'normal', dirname)
    # dirname = 'wallhaven-NSFW'
    # url_NSFW = 'https://wallhaven.cc/search?categories=111&purity=001&atleast=1920x1080&sorting=favorites&order=desc&page='
    # main(url_NSFW,'NSFW',dirname)
