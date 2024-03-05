import json
from fastapi import FastAPI
import urllib.request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/page2")
async def root():
    return {"message": "Page two"}

@app.get("/weather")
async def root():
    url = "http://ipinfo.io/json"
    response = urllib.request.urlopen(url)
    data = json.load(response)

    IP = data["ip"]
    org = data["org"]
    city = data["city"]
    country = data["country"]
    region = data["region"]

    return {"message": IP}