from urllib.parse import urlparse
import requests
import json

API_banned = 'https://reestr.rublacklist.net/api/v2/current/json'
API_availability = 'http://api.whois.vu/?q='


def loadInfo():
    response = requests.get(API_banned)
    if response.status_code == requests.codes.ok:
        JSON = response.json()
        return JSON
    else:
        print("Oops! Something unpredictable has happened")
        return None


def deserialization(JSON):
    URLS = []
    if JSON:
        for i in JSON:
            for j in JSON[str(i)]:
                if "https://" in j["link"]:
                    URLS.append(j["link"])
    return URLS


def checkAvailability(domain):
    avalability = requests.get(API_availability + domain)
    if avalability.status_code == requests.codes.ok:
        avalabilityJSON = avalability.json()
        return avalabilityJSON["available"]
    else:
        print("Oops! Something unpredictable has happened")
        return None


JSON = loadInfo()
URLS = deserialization(JSON)
for i in URLS:
    domain = urlparse(i).netloc
    availability = checkAvailability(i)
    if availability == "yes":
        print("Domain " + domain + " is available for purchasing")
    elif availability == "no":
        print("Domain " + domain + " isn't available for purchasing")
    elif availability == "undefined":
        print("There is no true info about " + domain)
    elif availability == "incorrect":
        print(domain + " can't be resolved")