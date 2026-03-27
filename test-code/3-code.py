import urllib3

http = urllib3.PoolManager(cert_reqs='CERT_NONE')  # SSL tekshiruvini o'chiradi
response = http.request('GET', 'https://example.com')
print(response.data.decode('utf-8'))