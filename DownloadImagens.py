import requests
link = (input('Insira o link:'))
r = requests.get(link)
with open('foto1.jpg', 'wb') as file:
    file.write(r.content)

