import requests
import json

url = "https://data.mongodb-api.com/app/data-zhpbu/endpoint/data/v1/action/findOne"

payload = json.dumps(
    {
        "collection": "Product",
        "database": "DataBike",
        "dataSource": "sandbox",
        "projection": {},
    }
)
headers = {
    "Content-Type": "application/json",
    "Access-Control-Request-Headers": "*",
    "api-key": "V1gBL7iLURWvrNu1nUM8unZFhX90uRkolBoi7d0TlnvgzOE9Kspgq3YC9XToW2oP",
    "Accept": "application/ejson",
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
