# Authentication

> SEO Bot expects an access token to be included in the header of each request made to the API. This header field is defined as follows:

```
Authorization: access-token
```

SEO Bot uses access tokens to authenticate requests made to the API. Each access token is linked to a single account and is only valid for one unique endpoint i.e. google, bing, yandex or duckduckgo.

Each account may have multiple access tokens across multiple endpoints, and the number of requests that may be made using these tokens will be based on the account limits.

When creating a new account, one token for each supported endpoint will be provided to you by default. To apply for an account, please visit our <a href="https://seobot.memberful.com/join">subscriptions</a> page to see available packages.

<aside class="info">
Token management through the API is currently under development and will be made available soon. In the interim, if you wish to create additional tokens or replace/delete existing tokens, please send your requests to <a href="mailto:admin@seobot.com">admin@seobot.com</a>.
</aside>

<aside class="warning">
Be careful when using or distributing your access tokens. Requests made using these tokens will be billed against the associated account.
</aside>