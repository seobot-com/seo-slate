# Codes

<aside class="notice">
This section details all possible response codes that may be returned by the API.
</aside>

Response codes and meanings:

Code | Meaning | Description
---- | ------- | -----------
200 | OK | The request was accepted and processed successfully.
400 | Bad Request | Your request is invalid.
401 | Unauthorized | Your API access token is wrong.
402 | Payment Required | You have reached the monthly request limit.
403 | Forbidden | The requested resource is hidden or available to administrators only.
404 | Not Found | The specified resource could not be found.
405 | Method Not Allowed | You tried to access a resource with an invalid method.
410 | Gone | The requested resource has been removed from our servers.
429 | Too Many Requests | You are making an unreasonable number of requests!
500 | Internal Server Error | We had a problem with our server. Try again later.
503 | Service Unavailable | We're temporarily offline for maintenance. Please try again later.
