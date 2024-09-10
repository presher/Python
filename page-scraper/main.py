import requests
import pandas as pd


url = "https://21ogkm5th5-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.17.0)%3B%20Browser"

payload = {}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,la;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://www.sunglasshut.com',
    'Referer': 'https://www.sunglasshut.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'x-algolia-api-key': 'dc91173a4a5d669a3eef474e5836e94f',
    'x-algolia-application-id': '21OGKM5TH5'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

res = []
for x in range(1, 12):
    querystring = {}
    headers = {}
    r = requests.request("GET", url, headers=headers, params=querystring)

    data = r.json()
    # chain together the elements neeeded
    for p in data['plpView']['products']['products']['product']:
        res.append(p)

df = pd.json_normalize(res)

df.to_csv('firsr_results.csv')
