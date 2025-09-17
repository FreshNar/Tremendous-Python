## Initialization
Before we can make any requests, we need to initialize the client. Every request follows the same schema. 

``` python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="<your-api-key>", sandbox=True)

tremendous.<resource>.<method(paramters)>
```

#### Working Example
``` python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="<your-api-key>", sandbox=True)

tremendous.Rewards.list(offset=0, limit=10)
```
For production enviornments, set Sandbox to False and replace your API Key with the production API Key.

::: tremendous.Rewards
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Orders
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Products
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Campaigns
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.FundingSources
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Invoices
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Topups
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.BalanceTransactions
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Organizations
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Members
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Roles
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Fields
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Webhooks
    handler: python
    rendering:
        show_root_heading: true
        show_source: false

::: tremendous.Forex
    handler: python
    rendering:
        show_root_heading: true
        show_source: false