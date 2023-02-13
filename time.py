from bs4 import BeautifulSoup
import requests

url_0 = requests.get('https://www.horario-brasilia.com')

url_text_0 = url_0.text

soup_0 = BeautifulSoup(url_text_0, 'html.parser')

time = soup_0.find(id="hora").get_text()

day = soup_0.find('strong').string

identifier = int(time[0:2])

if identifier >= 18:
  print(f"Hoje é {day}, e o horário é {time} da noite.")
elif identifier >= 12:
  print(f"Hoje é {day}, e o horário é {time} da tarde.")
elif identifier >= 5:
  print(f"Hoje é {day}, e o horário é {time} da manhã.")
elif identifier >= 00:
  print(f"Hoje é {day}, e o horário é {time} da madrugada.")