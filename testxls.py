# -*- coding:utf-8 -*-
import requests
import urllib, urllib2, json
import cookielib
import ssl
import xlwt
import xlrd

def write_excel():
    wk = xlwt.Workbook()
    st = wk.add_sheet('sheetname', cell_overwrite_ok=True)
    row0 = [u'主机名', u'主机IP', u'主机wwn', u'lun名称', u'lun_ID', u'lun 大小', u'lun_wwn']
    for i in range(0, len(row0)):
        st.write(0, i, row0[i])
    wk.save('demo3.xls')
    print('a')
    return
if __name__ == '__main__':
    write_excel()
