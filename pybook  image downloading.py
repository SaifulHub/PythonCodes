import requests
r = requests.get("https://images.unsplash.com/photo-1495344517868-8ebaf0a2044a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")
with open("wallpaper.png","wb") as i:
    i.write(r.content)