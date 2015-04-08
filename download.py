#!/usr/bin/env python

'''
this is a practice of python follow 'http://python.jobbole.com/81260/'
a tool whice can download hot photo in renren.com
'''

import json
import urllib
import os
print os.path.abspath('.')
def get_links():
    req=urllib.urlopen('https://api.renren.com/v2/share/hot/list?access_token=475780|6.bf3041f55a62900ecdeaf9bdaf9a6690.2592000.1431000000-483066716&shareType=TYPE_PHOTO')
  #  data=json.loads((req.read()).decode('utf-8'))
    f=open('/home/samoye/python/catch_hot_photo/out','w')
    f.write(req.read())
    f.close()
#    return data

def download_links(directory,link):
    image=urllib.urlretrieve(link,directory)

def set_download_dir():
    abspath=os.path.abspath('.')
    images_download=os.path.join(abspath,'image_download')
    if not os.path.exists(images_download):
        os.mkdir(images_download)
    return images_download

print get_links()
#url='http://a2.att.hudong.com/04/58/300001054794129041580438110_950.jpg'
#dire='/home/samoye/python/catch_hot_photo/2.jpg'
#download_links(dire,url)
