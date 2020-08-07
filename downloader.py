import sys
import requests
import os

#Disable Warning in case SSL failed
requests.packages.urllib3.disable_warnings();

#Set Max_Worker Limit
max_worker = 32;

#Create downloader Object for Each Download
class downloader:
    url='';
    fileSize='';

    def __init__(self,url):
        self.url = url;  
        self.fileSize = int(requests.get(self.url,stream=True,verify=False).headers['Content-Length'])
