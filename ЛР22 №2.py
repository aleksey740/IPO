import requests
import json

result = requests.get("https://swapi.dev/api/vehicles/4/")
json_dict = json.loads(result.text)
print(json_dict["cost_in_credits"])
