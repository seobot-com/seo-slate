# Regular search
curl 'http://example.com/google/search' \
     -H 'Content-Type: application/json' \
     -H 'Authorization: a5dc16c9d6fd89b30913d2bc988ad096' \
     -d '{
            "keywords": "seo bot api",
            "mobile"  : false,
            "type"    : "shop",

            "language": "en",
            "country" : "za",

            "start"   : 5,
            "num"     : 3
         }'

# Image search
curl 'http://example.com/google/images' \
     -H 'Content-Type: application/json' \
     -H 'Authorization: a5dc16c9d6fd89b30913d2bc988ad096' \
     -d '{
            "image_url": "https://images.example.com/image.jgp",
            "download" : false
         }'

# Reviews search
curl 'http://example.com/google/reviews' \
     -H 'Content-Type: application/json' \
     -H 'Authorization: a5dc16c9d6fd89b30913d2bc988ad096' \
     -d '{
            "fid"     : "{Feature ID}",
            "filter"  : "Nice food",
            "sort"    : "ratingHigh",

            "language": "en",
            "start"   : 5
         }'

# Trends search
curl 'http://example.com/google/trends' \
     -H 'Content-Type: application/json' \
     -H 'Authorization: a5dc16c9d6fd89b30913d2bc988ad096' \
     -d '{
            "keywords": "seo bot api",
            "category": 0,
            "type"    : "google",

            "language": "en",
            "country" : "za",

            "date"    : "now 7-d",
            "start"   : "2021-01-01",
            "stop"    : "2021-07-01"
         }'