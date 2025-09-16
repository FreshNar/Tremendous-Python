## Tremendous Python Client

A lightweight Python client for the Tremendous API. It provides convenient access to resources like orders, rewards, products, campaigns, funding sources, invoices, and more.

### Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

### Installation

If you're working from this repository directly:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Authentication and Environments

- Set your API key via an environment variable (recommended): `export TREMENDOUS_API_KEY=your_api_key`
- Initialize the client with `sandbox=True` to target the Tremendous sandbox; omit or set `False` for production.

### Quickstart

```python
import os
from tremendous import Tremendous

client = Tremendous(api_key=os.environ["TREMENDOUS_API_KEY"], sandbox=True)
```

### Usage Examples

1) List recent orders

```python
import os
from tremendous import Tremendous

client = Tremendous(api_key=os.environ["TREMENDOUS_API_KEY"], sandbox=True)

orders = client.orders.list(limit=5)
for order in orders:
    print(order.id, order.status, getattr(order, "created_at", None))
```

2) Create a simple order (email delivery)

```python
import os
from tremendous import Tremendous

client = Tremendous(api_key=os.environ["TREMENDOUS_API_KEY"], sandbox=True)

order = client.orders.create(
    payment_funding_source_id="fs_123456",  # your funding source ID
    recipient={
        "name": "Ada Lovelace",
        "email": "ada@example.com",
    },
    value={
        "denomination": 10.0,
        "currency_code": "USD",
    },
    products=[{"id": "prod_ABC123"}],  # a valid product ID from your account
    delivery_method={"method": "EMAIL"},
    external_id="order-001",
)

print(order.id, order.status)
```

3) Manage a reward (get, generate link, resend)

```python
import os
from tremendous import Tremendous

client = Tremendous(api_key=os.environ["TREMENDOUS_API_KEY"], sandbox=True)

# Retrieve an existing reward by ID
reward = client.rewards.get("rew_123456")
print(reward.id, reward.delivery.method, reward.recipient.email)

# Generate a redemption link for the reward
link_payload = client.rewards.generate_reward_url(reward.id)
print(link_payload)

# Resend the reward to a new email (only for previously failed deliveries)
client.rewards.resend_reward(reward.id, updated_email="new-email@example.com")
```

### Available Resources

The client exposes resource-specific helpers via attributes on the main client:

- `client.products`
- `client.rewards`
- `client.orders`
- `client.campaigns`
- `client.funding_sources`
- `client.invoices`
- `client.topups`
- `client.balance_transactions`
- `client.organizations`
- `client.members`
- `client.roles`
- `client.fields`
- `client.webhooks`
- `client.forex`

Each resource provides methods such as `get`, `list`, and where applicable `create`, `approve`, `reject`, or other actions.

### License

This project is licensed under the terms of the license found in `LICENSE`.

