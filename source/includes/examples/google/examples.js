/*
// Regular search
const fetch = require("node-fetch");

const payload = {
                "keywords": "seo bot api",
                "mobile"  : false,
                "type"    : "shop",

                "language": "en",
                "country" : "za",

                "start"   : 5,
                "num"     : 3
            };

fetch('https://api.seobot.com:11115/google/search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'a5dc16c9d6fd89b30913d2bc988ad096'
  },
  body: JSON.stringify(payload),
})
.then((response) => response.json())
.then((result) => {
  console.log('Response:', result);
})
.catch((error) => {
  console.error('Error:', error);
});

// Image search
const fetch = require("node-fetch");

const payload = {
              "image_url": "https://api.seobot.com:11115/google/images",
              "download" : false
            };

fetch('https://api.seobot.com:11115/google/images', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'a5dc16c9d6fd89b30913d2bc988ad096'
  },
  body: JSON.stringify(payload),
})
.then((response) => response.json())
.then((result) => {
  console.log('Response:', result);
})
.catch((error) => {
  console.error('Error:', error);
});

// Reviews search
const fetch = require("node-fetch");

const payload = {
             "fid"     : "{Feature ID}",
             "filter"  : "Nice food",
             "sort"    : "ratingHigh",

             "language": "en",
             "start"   : 5
            };

fetch('https://api.seobot.com:11115/google/reviews', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'a5dc16c9d6fd89b30913d2bc988ad096'
  },
  body: JSON.stringify(payload),
})
.then((response) => response.json())
.then((result) => {
  console.log('Response:', result);
})
.catch((error) => {
  console.error('Error:', error);
});

// Trends search
const fetch = require("node-fetch");

const payload = {
             "keywords": "seo bot api",
             "category": 0,
             "type"    : "google",

             "language": "en",
             "country" : "za",

             "date"    : "now 7-d",
             "start"   : "2021-01-01",
             "stop"    : "2021-07-01"
            };

fetch('http://localhost:54453/google/trends', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'a5dc16c9d6fd89b30913d2bc988ad096'
  },
  body: JSON.stringify(payload),
})
.then((response) => response.json())
.then((result) => {
  console.log('Response:', result);
})
.catch((error) => {
  console.error('Error:', error);
});
*/