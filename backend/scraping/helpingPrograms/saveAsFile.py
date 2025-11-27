import requests

def save_as_file(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

        
    