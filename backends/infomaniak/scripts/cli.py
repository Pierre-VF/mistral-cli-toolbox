# /// script
# dependencies = [
#   "requests",
#   "pydantic-settings",
# ]
# ///

import json

import requests
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    INFOMANIAK_AI_TOKEN: str
    INFOMANIAK_PROJECT_ID: str


load_dotenv()

s = _Settings()

# Get models
url = f"https://api.infomaniak.com/2/ai/{s.INFOMANIAK_PROJECT_ID}/openai/v1/models"
headers = {
    "Authorization": f"Bearer {s.INFOMANIAK_AI_TOKEN}",
    "Content-Type": "application/json",
}
req = requests.request("GET", url=url, headers=headers)
res = req.json()
print(json.dumps(res, indent=3))
