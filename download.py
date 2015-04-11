#!/usr/bin/env python

'''
this is a practice of python follow 'http://python.jobbole.com/81260/'
a tool whice can download hot photo in renren.com
'''

import json
import urllib
import os
def get_links(api_url):  
    req=urllib.urlopen(api_url)
    data=json.loads((req.read()).decode('utf-8'))
    return data
    

def download_links(directory,link,name):
    download_path=os.path.join(directory,name)
    image=urllib.urlretrieve(link,download_path)

def set_download_dir():
    abspath=os.path.abspath('.')
    images_download=os.path.join(abspath,'image_download')
    if not os.path.exists(images_download):
        os.mkdir(images_download)
    return images_download

#url='http://fmn.rrfmn.com/fmn064/20141221/1415/head_BzLf_684300013146118c.jpg'
#download_dir=set_download_dir()
#name='%d' % 2+'.jpg'
#print name
#download_links(download_dir,url,name)
#url='http://a2.att.hudong.com/04/58/300001054794129041580438110_950.jpg'
#dire='/home/samoye/python/catch_hot_photo/2.jpg'
#download_links(dire,url)
