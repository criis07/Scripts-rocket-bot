import requests
import json
from bs4 import BeautifulSoup

var_rocket = '{url}'
url = 'https://jsonplaceholder.typicode.com/posts/' if var_rocket else ''
r = requests.get(url)
posts = r.json()
formatted_json = json.loads(json.dumps(posts[-10:], indent=4))

var_rocket2 = '{url_titulos}'
url2 = 'https://scrapingclub.com/exercise/list_basic/?page=1' if var_rocket2 else ''

response = requests.get(url2)
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all('div', class_='w-full rounded border')

array = []
elementos = 0

for post in posts:
    # Encontrar el h4 dentro del div
    h4_tag = post.find('h4')

    if h4_tag:
        # Encontrar el enlace dentro del h4
        a_tag = h4_tag.find('a')

        if a_tag:
            # Obtener el texto dentro de la etiqueta <a>
            link_text = a_tag.text.strip()

            # Incrementar el contador 
            elementos += 1

            # Si se ha alcanzado el límite del bucle, salir del bucle
            if elementos == 11:
                break

            array.append(link_text)

# Actualizar los títulos de formatted_json
for i, item in enumerate(formatted_json):
# Verificar si hay elementos en el array de títulos
    if i < len(array):
        item['title'] = array[i]
        item['body'] = formatted_json[i]['body'].replace("\n", " ")
        
formatted_json = [[dic[key] for key in dic] for dic in formatted_json]
formatted_json.insert(0, ['userId', 'id','title','body'])       

SetVar('titulos_reemplazados', formatted_json)
