## Python client library for the Tremendous API

A simple and lightweight Python client for the Tremendous API. It provides convenient access to resources like orders, rewards, products, campaigns, funding sources, invoices, and more. 

[Tremendous API Reference](https://developers.tremendous.com/reference/rewards)

### Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

### Quickstart
You'll need a Tremendous API Key to get started. You can get started with the [Sandbox here](https://developers.tremendous.com/docs/1-create-a-sandbox-account). 

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)
```
