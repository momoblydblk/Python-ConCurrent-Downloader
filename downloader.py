import sys
import requests
import os

#Disable Warning in case SSL failed
requests.packages.urllib3.disable_warnings();

#Set Max_Worker Limit
max_worker = 32;

def init(self,url):
    self.url = url;
    r1 = requests.get(url, stream=True, verify=False);
    self.size = int(r1.headers['Content-Length']);
    
