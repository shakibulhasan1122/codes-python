import re
import requests
import urllib.request

link=input("Enter Link: ")

html=requests.get(link)

try:
    url=re.search('hd_src:"(.+?)"',html.text)[-1]
    print("HD Video")
except:
    url=re.search('sd_src:"(.+?)"',html.text)[-1]
    print("SD Video")

print("Downloading...")
urllib.request.urlretrieve(url, "Facebook Video.mp4")
print("Download Successfull!")
