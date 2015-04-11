#/usr/bin/enc python
#download phosts

import os
import json
import time
import ConfigParser
from download import set_download_dir,get_links,download_links
def main():
    download_dir=set_download_dir()
    url=ConfigParser.ConfigParser()
    url.readfp(open('api_url.ini','rw'))
    api_url=url.get('api','api_url1')
    links={'%d' % l['id']:l['thumbUrl'] for l in get_links(api_url)['response']}
    api_url=url.get('api','api_url2')
    for l in get_links(api_url)['response']:
        links['%d' % l['id']]=l['thumbUrl']
    api_url=url.get('api','api_url3')
    for l in get_links(api_url)['response']:
        links['%d' % l['id']]=l['thumbUrl']
    i=0
    time1=time.time()
    for link in links:
        name=link+'.jpg'
        download_links(download_dir,links[link],name)
 	i=i+1
    time2=time.time() 
    print time2-time1
    print 'the number of photos is %d' % i
if __name__=='__main__':
    main() 
