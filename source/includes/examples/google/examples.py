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

             "start"   : 0,
             "num"     : 10
         }

request = requests.post('https://api.seobot.com:11115/google/search',
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

request = requests.post('https://api.seobot.com:11115/google/images',
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
            "start"   : 0
         }

request = requests.post('https://api.seobot.com:11115/google/reviews',
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

request = requests.post('https://api.seobot.com:11115/google/trends',
                        headers={'Authorization': api_token},
                        json=payload)
result = json.loads(request.text)