*From Tremendous API Docs*: [https://developers.tremendous.com/docs/error-handling](https://developers.tremendous.com/docs/error-handling)

| HTTP status code | Meaning |
|-----------------|---------|
| 200 | API request successful |
| 201 | This HTTP is only returned when an order with a duplicate `external_id` is submitted. It indicates that the order already exists. |
| 202 | API request successful (no new resource created yet, but new resource will be created asynchronously in the background) |
| 400 | Validation error of the sent parameters or request body |
| 401 | Authorization error e.g. due to an invalid or missing API key |
| 402 | Not enough funds in your account |
| 404 | No resource could be found for the provided ID |
| 422 | Request lacks one of the required parameters |
| 429 | Rate limit exceeded |
| 500 | Unexpected error. If this persists, please contact developers@tremendous.com |
| 502 | Temporary gateway error—service unreachable. Retry, and let us know if it continues. |
