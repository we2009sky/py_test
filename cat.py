import os
import urllib.request

res = urllib.request.urlopen('http://placekitten.com/700/700')cat_img = res.read()

with open('cat_600_700.jpg', 'wb') as f:
    f.write(cat_img)
print(os.getcwd())
