# Regular search
import requests
import json

api_token = 'a5dc16c9d6fd89b30913d2bc988ad096'
payload = {
             "keywords": "seo bot api",
             "mobile"  : False,
             "type"    : "shop",

             "language": "en",
             "country" : "za",

             "start"   : 5,
             "num"     : 3
         }

request = requests.post('http://example.com/google/search',
                        headers={'Authorization': api_token},
                        json=payload)
result = json.loads(request.text)

# Image search
import requests
import json

api_token = 'a5dc16c9d6fd89b30913d2bc988ad096'
payload = {
             "image_url": "https://images.example.com/image.jgp",
             "download" : False
         }

request = requests.post('http://example.com/google/images',
                        headers={'Authorization': api_token},
                        json=payload)
result = json.loads(request.text)

# Reviews search
import requests
import json

api_token = 'a5dc16c9d6fd89b30913d2bc988ad096'
payload = {
            "fid"     : "{Feature ID}",
            "filter"  : "Nice food",
            "sort"    : "ratingHigh",

            "language": "en",
            "start"   : 5
         }

request = requests.post('http://example.com/google/reviews',
                        headers={'Authorization': api_token},
                        json=payload)
result = json.loads(request.text)

# Trends search
import requests
import json

api_token = 'a5dc16c9d6fd89b30913d2bc988ad096'
payload = {
             "keywords": "seo bot api",
             "category": 0,
             "type"    : "google",

             "language": "en",
             "country" : "za",

             "date"    : "now 7-d",
             "start"   : "2021-01-01",
             "stop"    : "2021-07-01"
         }

request = requests.post('http://example.com/google/trends',
                        headers={'Authorization': api_token},
                        json=payload)
result = json.loads(request.text)