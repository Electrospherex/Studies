import requests
link = (input('Insira o link:'))
r = requests.get(link)
with open('fotoo1.jpg', 'wb') as file:
    file.write(r.content)

