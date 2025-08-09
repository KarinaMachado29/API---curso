import requests
id = 23
url = f"https://67efe7452a80b06b8896368d.mockapi.io/camisa/{id}"

data = {
    "nome":"Karina",
    "marca": "Morena Rosa",
    "preco": 109.01,
    "tamanho": "M"
}

response = requests.put(url, json= data)

if response.status_code ==200:
    atualizado  = response.json()
    print(f"Usuário com ID {id} foi atualizado com sucesso😊")
    print (atualizado)
else:
 print (f"Falha na requisição😒: {response.status_code}{response.text}")      
