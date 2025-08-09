import requests
url = "https://67efe7452a80b06b8896368d.mockapi.io/camisa"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    
    for post in posts [:10]:
       print(post)          
else:
 print (f"Falha na requisição:{response.status_code}{response.text}")  
    

