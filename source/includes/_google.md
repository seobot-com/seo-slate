# Google

## Search by Text

> An example of a search-by-text request is given below:

```shell
# Ensure that the data being supplied is in a valid json format
curl 'http://example.com/google/search' \
     -H 'Content-Type: application/json' \
     -d '{
             "keywords": "seo bot api",
             "mobile"  : false,
             "type"    : "shop",

             "langauge": "en",
             "country" : "za",
             "uule"    : "w+CAIQICIfUHJldG9yaWEsIEdhdXRlbmcsIFNvdXRoIEFmcmljYQ",

             "start"   : 5,
             "num"     : 3
         }'
```

```python
import requests
import json

payload = {
             "keywords": "seo bot api",
             "mobile"  : False,
             "type"    : "shop",

             "language": "en",
             "country" : "za",
             "uule"    : "w+CAIQICIfUHJldG9yaWEsIEdhdXRlbmcsIFNvdXRoIEFmcmljYQ",

             "start"   : 5,
             "num"     : 3
         }

request = requests.post('http://example.com/google/search', json=payload)

# This line is optional, request.text() will return the result as a JSON formatted string
result = json.loads(request.text())
```

```go
payload := strings.NewReader(`{
             "keywords": "seo bot api",
             "mobile"  : False,
             "type"    : "shop",

             "language": "en",
             "country" : "za",
             "uule"    : "w+CAIQICIfUHJldG9yaWEsIEdhdXRlbmcsIFNvdXRoIEFmcmljYQ",

             "start"   : 5,
             "num"     : 3
         }`)

request, err := http.NewRequest("POST", "http://example.com/google/search", payload)
if err != nil {
  // Error handling...
}
request.Header.Set("Content-Type", "application/json")

client := &http.Client{}
response, err := client.Do(request)
if err != nil {
  // Error handling...
}
  
var result string
err := json.NewDecoder(resp.Body).Decode(&response)
if err != nil {
  // Error handling...
}
// result now contains the response body as a JSON formatted string
```

```javascript
const fetch = require("node-fetch");

const payload = {
                "keywords": "seo bot api",
                "mobile"  : false,
                "type"    : "isch",

                "language": "en",
                "country" : "za",
                "uule"    : "w+CAIQICIfUHJldG9yaWEsIEdhdXRlbmcsIFNvdXRoIEFmcmljYQ",

                "start"   : 5,
                "num"     : 3
            };

fetch('http://localhost:54453/google/search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(payload),
})
.then((response) => response.json())
.then((result) => {
  console.log('Result:', result);
})
.catch((error) => {
  console.error('Error:', error);
});
```

> The above command returns a JSON object structured like this:

```json
[
  {
    "id": 1,
    "name": "Fluffums",
    "breed": "calico",
    "fluffiness": 6,
    "cuteness": 7
  },
  {
    "id": 2,
    "name": "Max",
    "breed": "unknown",
    "fluffiness": 5,
    "cuteness": 10
  }
]
```

This endpoint performs a regular Google search-by-text and returns the results in json format. The type and number of results returned depends on the request's parameters.

### HTTP Endpoint

`GET http://example.com/google/search`

### Search Parameters

Parameter | Type | Required | Description
--------- | -----| -------- | -----------
keywords  |String| Yes      | Keywords for which to search
mobile    | Bool | No       | Indicates whether the user-agent is a mobile or desktop device (Default: false)
type      |String| No       | Used to set the search type (Default: all) </br> <u>Available Options:</u> </br>&bull; `shop` -> Shopping </br>&bull; `isch` -> Images </br>&bull; `nws` -> News </br>&bull; `jobs` -> Jobs

### Localization parameters

Parameter | Type | Required | Description
--------- | ---- | -------- | -----------
language  |String| No       | Two-letter language code to indicate search language
country   |String| No       | Two-letter country code to indicate search country
uule      |String| No       | Encoded location from which to search. A list of valid locations can be found <a href="https://developers.google.com/adwords/api/docs/appendix/geotargeting"> here</a>

### Pagination parameters

Parameter | Type | Required | Description
--------- | ---- | -------- | -----------
start     | Int  | No       | Indicates the offset of the first result to be returned (Default: 0)
num       | Int  | No       | Indicates the number of results to be returned after the starting offset (Default: 10)

<aside class="info">
Note — any parameters included in the request that are not specified in the tables above will be ignored
</aside>

## Search by Image

This endpoint performs a Google search-by-image and returns the results in json format.

### HTTP Endpoint

`GET http://example.com/google/images`

### Search Parameters

Parameter | Type | Required | Description
--------- | -----| -------- | -----------
image_url |String| Yes      | URL of the image on which the search will be based
download  | Bool | No       | Indicates whether to perform a regular GET request or to perform a POST request to google with the requested image URL (Default: false)

<aside class="info">
Note — any parameters included in the request that are not specified in the tables above will be ignored
</aside>

## Reviews

This endpoint performs a Google search of all reviews for a specific feature and returns the results in json format. The type and number of results returned depends on the request's parameters.

### HTTP Endpoint

`GET http://example.com/google/reviews`

### Search Parameters

Parameter | Type | Required | Description
--------- | -----| -------- | -----------
fid       |String| Yes      | Feature ID for which reviews will be fetched
filter    |String| No       | Filter keywords, which will only return results that contain the given keywords
sort      |String| No       | The order in which the reviews are sorted (Default: Most Relevant First) </br> <u>Available Options:</u> </br>&bull; `qualityScore` -> Most relevant first </br>&bull; `newestFirst` -> Newest first </br>&bull; `ratingHigh` -> Highest rating first </br>&bull; `ratingLow` -> Lowest rating first

### Localization and Pagination parameters

Parameter | Type | Required | Description
--------- | ---- | -------- | -----------
language  |String| No       | Two-letter language code to indicate search language
start     | Int  | No       | Indicates the offset of the first result to be returned (Default: 0)

<aside class="info">
Note — any parameters included in the request that are not specified in the tables above will be ignored
</aside>

## Trends

This endpoint performs a Google trends search and returns the results in json format. The type and number of results returned depends on the request's parameters.

### HTTP Endpoint

`GET http://example.com/google/trends`

### Search Parameters

Parameter | Type | Required | Description
--------- | -----| -------- | -----------
keywords  |String| Yes      | Keywords for which to search
category  | Int  | No       | The id of the category in which to search </br>(Default: 0). A list of all categories can be found <a href="https://trends.google.com/trends/api/explore/pickers/category"> here</a>
type      |String| No       | Used to set the search type (Default: Web Search) </br> <u>Available Options:</u> </br>&bull; `images` -> Images </br>&bull; `news` -> News </br>&bull; `google` -> Google </br>&bull; `youtube` -> Google

### Localization parameters

Parameter | Type | Required | Description
--------- | ---- | -------- | -----------
language  |String| No       | Two-letter language code to indicate search language
country   |String| No       | Two-letter country code to indicate search country

### Timerange parameters

Parameter | Type | Required | Description
--------- | ---- | -------- | -----------
date      |String| No       | The time range in which to search (Default: Past 12 Months) </br> <u>Available Options:</u> </br>&bull; `now 1-H` - Past hour </br>&bull; `now 4-H` - Past 4 hours </br>&bull; `now 1-d` - Past day </br>&bull; `now 7-d` - Past week </br>&bull; `today 1-m` - Past month </br>&bull; `today 3-m` - Past 3 months </br>&bull; `today 12-m` - Past 12 months </br>&bull; `today 5-y` - Past 5 years
start     |String| No       | A custom start date from which to query (Format: `YYYY-MM-DD`). This parameter is ignored if the **_stop_** parameter is not set
stop      |String| No       | A custom stop date from which to query (Format: `YYYY-MM-DD`). This parameter is ignored if the **_start_** parameter is not set

<aside class="info">
Note — any parameters included in the request that are not specified in the tables above will be ignored
</aside>