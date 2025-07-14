import multiprocessing
import requests

def downloadfile(url,name):
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)

url = "https://picsum.photos/200/300"

for i in range(5):
    downloadfile(url, i)




