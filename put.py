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

print(response.status_code)
print(response.text)