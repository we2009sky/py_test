import os
import urllib.request

res = urllib.request.urlopen('http://placekitten.com/800/800')
cat_img = res.read()

with open('cat_800_800.jpg', 'wb') as f:
    f.write(cat_img)
print(os.getcwd())  
