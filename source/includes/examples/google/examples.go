package main

/*
// Regular search
import (
	"encoding/json"
	"net/http"
	"strings"
)

payload := strings.NewReader(`{
             "keywords": "seo bot api",
             "mobile"  : False,
             "type"    : "shop",

             "language": "en",
             "country" : "za",

             "start"   : 5,
             "num"     : 3
         }`)

request, err := http.NewRequest("POST",
    "https://api.seobot.com:11115/google/search",
    payload)
if err != nil {
  // Error handling...
}
request.Header.Set("Authorization", "a5dc16c9d6fd89b30913d2bc988ad096")
request.Header.Set("Content-Type", "application/json")

client := &http.Client{}
response, err := client.Do(request)
if err != nil {
  // Error handling...
}

result map[string]interface{}{}
err := json.NewDecoder(response.Body).Decode(&result)
if err != nil {
  // Error handling...
}

// Image search
import (
    "encoding/json"
    "net/http"
    "strings"
)

payload := strings.NewReader(`{
             "image_url": "https://images.example.com/image.jgp",
             "download" : false
         }`)

request, err := http.NewRequest("POST",
    "https://api.seobot.com:11115/google/images",
    payload)
if err != nil {
  // Error handling...
}
request.Header.Set("Authorization", "a5dc16c9d6fd89b30913d2bc988ad096")
request.Header.Set("Content-Type", "application/json")

client := &http.Client{}
response, err := client.Do(request)
if err != nil {
  // Error handling...
}

result map[string]interface{}{}
err := json.NewDecoder(response.Body).Decode(&result)
if err != nil {
  // Error handling...
}

// Reviews search
import (
    "encoding/json"
    "net/http"
    "strings"
)

payload := strings.NewReader(`{
            "fid"     : "{Feature ID}",
            "filter"  : "Nice food",
            "sort"    : "ratingHigh",

            "language": "en",
            "start"   : 5
         }`)

request, err := http.NewRequest("POST",
    "https://api.seobot.com:11115/google/reviews",
    payload)
if err != nil {
  // Error handling...
}
request.Header.Set("Authorization", "a5dc16c9d6fd89b30913d2bc988ad096")
request.Header.Set("Content-Type", "application/json")

client := &http.Client{}
response, err := client.Do(request)
if err != nil {
  // Error handling...
}

result map[string]interface{}{}
err := json.NewDecoder(response.Body).Decode(&result)
if err != nil {
  // Error handling...
}

// Trends search
import (
    "encoding/json"
    "net/http"
    "strings"
)

payload := strings.NewReader(`{
             "keywords": "seo bot api",
             "category": 0,
             "type"    : "google",

             "language": "en",
             "country" : "za",

             "date"    : "now 7-d"
             "start"   : "2021-01-01",
             "stop"    : "2021-07-01"
         }`)

request, err := http.NewRequest("POST",
    "https://api.seobot.com:11115/google/trends",
    payload)
if err != nil {
  // Error handling...
}
request.Header.Set("Authorization", "a5dc16c9d6fd89b30913d2bc988ad096")
request.Header.Set("Content-Type", "application/json")

client := &http.Client{}
response, err := client.Do(request)
if err != nil {
  // Error handling...
}

result map[string]interface{}{}
err := json.NewDecoder(response.Body).Decode(&result)
if err != nil {
  // Error handling...
}
*/
