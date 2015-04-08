import os
import json
from download import set_download_dir,get_links,download_links
# download_dir=set_download_dir()
#    links=[l for l in get_links() if l.endswith('.jpg')]
f=open('/home/samoye/python/catch_hot_photo/out','r')
data=json.loads((f.read()).decode('utf-8'))
f.close()
links=[l['thumbUrl'] for l in data['response']]
print links
