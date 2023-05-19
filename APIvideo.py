import requests

r = requests.post('https://api.json2video.com/v2/movies', headers = {"x-api-key":'Mm6GqzCPnX533SB6ipTU229x1SZA6fTt40YtusIk', 'Content-Type': 'text/plain'})
"""--header 'x-api-key: [[YOUR_APIKEY]]' 
--header 'Content-Type: application/json' 
--data-raw '[[YOUR_JSON]]'"""
print(r.json)