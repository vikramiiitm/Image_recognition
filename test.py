import requests

url = "https://api.edenai.run/v2/image/object_detection"

headers = {
  "Content-Type": "multipart/form-data",
  "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTE4YTdiMzktNDM1Ny00N2UxLWI4ZTEtYjI5MDNiZmJiNTQ2IiwidHlwZSI6ImFwaV90b2tlbiJ9.ua1nj6zjyFtH72Duzl9BX72fB0_fpscX111WNJwi84A"
}

response = requests.post(url, headers=headers)

data = response.json()
print(data)