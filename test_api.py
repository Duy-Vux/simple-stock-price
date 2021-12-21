import json
import requests 

strAPI = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2020-08-12&end_date=2020-08-12&api_key=gx1daXuj2m8vbtrVKtHALsIVu8U2yvBOWcbyjch8"

response = requests.get(strAPI)

json_data = json.loads(response.text)

print(json_data["links"]["prev"])