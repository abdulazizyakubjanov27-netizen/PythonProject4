import requests
import certifi

url = "https://www.python.org"
response = requests.get(url, verify=certifi.where())  # SSL sertifikatini tekshiradi
print(response.text[:200])