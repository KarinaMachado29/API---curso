import requests
url = "https://67efe7452a80b06b8896368d.mockapi.io/camisa"

data = {
    "nome":"Karina",
    "marca": "Adidas",
    "preco": 59.00,
    "tamanho": "M"
}

response = requests.post(url, json=data)
if response.status_code == 201:
    new_post = response.json()
    print("Novo post criado!!!")
    print(new_post)
else:
 print (f"Falha na requisição:{response.status_code}{response.text}")  
    