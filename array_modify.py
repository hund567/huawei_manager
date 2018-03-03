

# -*- coding:utf-8 -*-
import requests
import urllib, urllib2, json
import cookielib
import ssl
import xlwt
import xlrd

def func(array_ip, array_id, iBaseToken):


    url_head = 'https://' + array_ip + ':8088/deviceManager/rest/'
    upload_url = url_head + 'xxxxx/login' + array_id + '/file/buildrun/Upload?iBaseToken=' + iBaseToken

    files = {'file':open('example.conf','rb')}
    data = {}

    # data 方式传表单

    # header 文件头

    # file传送multipart

    # content-type在header中写明

    user_agent = r'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'

    head = {'User-Agent': user_agent, 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryXhMAt19sI1bjb2Rm ',
            'Host':array_ip, 'Origin':'https://' + array_ip + ':8088 ', 'Upgrade-Insecure-Requests': bytes(1),
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br'}

    r = requests.post(url=upload_url, file=files, header = head, verify=False)