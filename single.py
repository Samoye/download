import os
import json
import time
from download import set_download_dir,get_links,download_links
def main():
    download_dir=set_download_dir()
    links=get_links()
    i=0
    print "time0:%s" % time.clock()
    for link in links:
        name='%d' % i+'.jpg'
        download_links(download_dir,link,name)
 	i=i+1
	print "time:%s" % time.clock()

 
if __name__=='__main__':
    main() 
