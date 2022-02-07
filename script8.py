import requests

url = "https://delo-stats.azurewebsites.net/api/decentratokens-stats?code=1&token=DFEG"


resp = requests.get(url)

print(resp.json())