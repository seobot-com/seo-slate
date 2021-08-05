---
title: SEOBot API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell
  - python
  - golang
  - javascript

toc_footers:
  - <a href='#'>Sign Up for a Developer Key</a>
  - <a href='https://github.com/slatedocs/slate'>Documentation Powered by Slate</a>

includes:
  - errors

search: true

code_clipboard: true
---

# Introduction

Insert sample text here ;3.

# Google
 
 Describe google search engine endpoint here

## Regular Search

Describe regular search here

### HTTP Request

`GET http://example.com/google/search`

### Query Parameters

Parameter | Type | Required | Default | Description
--------- | ---- | -------- | --------| -----------
keywords  |String| Yes      | N/A     ||
langauge  |String| No       | N/A     ||
country   |String| No       | N/A     ||
mobile    | Bool | No       | false   ||
start     | Int  | No       | 0       ||
uule      |String| No       | None    ||
type      |String| No       | Regular ||
num       | Int  | No       | 10      ||

<aside class="info">
Note — any parameters included in the request that are not specified in the table above will be ignored!
</aside>

## Search by Image

Describe image search here

### HTTP Request

`GET http://example.com/google/images`

### Query Parameters

Parameter | Type | Required | Default | Description
--------- | ---- | -------- | --------| -----------
image_url |String| Yes      | N/A     ||
download  | Bool | No       | N/A     ||

<aside class="info">
Note — any parameters included in the request that are not specified in the table above will be ignored!
</aside>

## Maps

Describe maps search here

### HTTP Request

`GET http://example.com/google/maps`

### Query Parameters

Parameter | Type | Required | Default | Description
--------- | ---- | -------- | --------| -----------
keywords  |String| Yes      | N/A     ||
langauge  |String| No       | N/A     ||
country   |String| No       | N/A     ||
start     | Int  | No       | N/A     ||
num       | Int  | No       | N/A     ||

<aside class="info">
Note — any parameters included in the request that are not specified in the table above will be ignored!
</aside>

## Reviews

Describe reviwes search here

### HTTP Request

`GET http://example.com/google/reviews`

### Query Parameters

Parameter | Type | Required | Default | Description
--------- | ---- | -------- | --------| -----------
langauge  |String| No       | N/A     ||
filter    |String| No       | N/A     ||
start     | Int  | No       | N/A     ||
sort      |String| No       | N/A     ||
fid       |String| Yes      | N/A     ||


<aside class="info">
Note — any parameters included in the request that are not specified in the table above will be ignored!
</aside>

## Trends

Describe trends search here

### HTTP Request

`GET http://example.com/google/trends`

### Query Parameters

Parameter | Type | Required | Default | Description
--------- | ---- | -------- | --------| -----------

keywords  |String| Yes      | N/A     ||
category  |String| No       | N/A     ||
langauge  |String| No       | N/A     ||
country   |String| No       | N/A     ||
start     |String| No       | N/A     ||
stop      |String| No       | N/A     ||
date      |String| No       | N/A     ||
type      |String| No       | N/A     ||

<aside class="info">
Note — any parameters included in the request that are not specified in the table above will be ignored!
</aside>

# Bing

# Yandex

# DuckDuckGo

> To authorize, use this code:

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
```

```shell
# With shell, you can just pass the correct header with each request
curl "api_endpoint_here" \
  -H "Authorization: meowmeowmeow"
```

```javascript
const kittn = require('kittn');

let api = kittn.authorize('meowmeowmeow');
```

> Make sure to replace `meowmeowmeow` with your API key.

Kittn uses API keys to allow access to the API. You can register a new Kittn API key at our [developer portal](http://example.com/developers).

Kittn expects for the API key to be included in all API requests to the server in a header that looks like the following:

`Authorization: meowmeowmeow`

<aside class="notice">
You must replace <code>meowmeowmeow</code> with your personal API key.
</aside>

# Kittens

## Get All Kittens

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.get
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.get()
```

```shell
curl "http://example.com/api/kittens" \
  -H "Authorization: meowmeowmeow"
```

```javascript
const kittn = require('kittn');

let api = kittn.authorize('meowmeowmeow');
let kittens = api.kittens.get();
```

> The above command returns JSON structured like this:

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

This endpoint retrieves all kittens.

### HTTP Request

`GET http://example.com/api/kittens`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
include_cats | false | If set to true, the result will also include cats.
available | true | If set to false, the result will include kittens that have already been adopted.

<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Kitten

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.get(2)
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.get(2)
```

```shell
curl "http://example.com/api/kittens/2" \
  -H "Authorization: meowmeowmeow"
```

```javascript
const kittn = require('kittn');

let api = kittn.authorize('meowmeowmeow');
let max = api.kittens.get(2);
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "name": "Max",
  "breed": "unknown",
  "fluffiness": 5,
  "cuteness": 10
}
```

This endpoint retrieves a specific kitten.

<aside class="warning">Inside HTML code blocks like this one, you can't use Markdown, so use <code>&lt;code&gt;</code> blocks to denote code.</aside>

### HTTP Request

`GET http://example.com/kittens/<ID>`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the kitten to retrieve

## Delete a Specific Kitten

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.delete(2)
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.delete(2)
```

```shell
curl "http://example.com/api/kittens/2" \
  -X DELETE \
  -H "Authorization: meowmeowmeow"
```

```javascript
const kittn = require('kittn');

let api = kittn.authorize('meowmeowmeow');
let max = api.kittens.delete(2);
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "deleted" : ":("
}
```

This endpoint deletes a specific kitten.

### HTTP Request

`DELETE http://example.com/kittens/<ID>`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the kitten to delete

