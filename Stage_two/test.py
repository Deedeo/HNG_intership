import requests


response = requests.get('https://hng-nameapp.onrender.com/api')
print(response.json())