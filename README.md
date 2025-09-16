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

### Usage Examples

1) List recent orders

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

orders = tremendous.orders.list(limit=5)
for order in orders:
    print(order.id, order.status, order.rewards)
```

2) Create a simple order (email delivery)

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

order = tremendous.orders.create(
    payment_funding_source_id="balance", 
    campaign_id="ABCDEF12345", 
    value={
        "denomination": 100, 
        "currency_code": "USD"
    }, 
    recipient={
        "name": "Jake Smith", 
        "email": "jsmith@example.com"
    }, 
    language="en",
    delivery_method={"method": "email"},
    meta_data=[
        {
            "test_meta_data": "test_meta_data", 
            "test_meta_data_2": "test_meta_data_2"
        }
    ]
)

```

3) Update an existing campaign

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

campaign = tremendous.campaigns.update(
    id="ABCDEF123456",
    name="My New Campaign",
    description="A test campaign",
    webpage_style={
        "headline": "Hello World!", 
        "message": "Thank you for your support!", 
        "logo_image_height_px": 100, 
        "logo_background_color": "#121212", 
        "background_color": "#121212"
    },
    email_style={
        "sender_name": "John Smith",
        "subject_line": "Hello World - Thank you for your support!",
        "logo_image_height_px": 100,
        "logo_background_color": "#121212",
        "button_color": "#121212"
    }
)
```

### Available Resources

The client exposes resource-specific helpers via attributes on the main client:

#### Rewards

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# Get Reward from ID
tremendous.rewards.get(id='ABCD123')

# List Rewards
tremendous.rewards.list(offset=0, limit=100)

# Generate Reward URL
tremendous.rewards.generate_reward_url(id='ABCD123')

# Resend Reward 
tremendous.rewards.resend_reward(
    id='ABCD123', 
    updated_email='ssmith@example.com', 
    updated_phone='3215555555'
)

# Cancel Reward
tremendous.rewards.cancel_reward(id='ABCD123')

```

#### Orders

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# Get Order from ID
tremendous.orders.get(order_id='ABCD123')

# List Orders
tremendous.orders.list(
    offset=0, 
    campaign_id='CAMP123', 
    external_id='EXT123', 
    created_at_gte='2024-01-01', 
    created_at_lte='2024-12-31', 
    limit=10
)

# Create Order
tremendous.orders.create(
    payment_funding_source_id='balance',
    recipient={
        'name': 'Jane Doe', 
        'email': 'jdoe@example.com'
    },
    value={
        'denomination': 50, 
        'currency_code': 'USD'
    },
    campaign_id='CAMP123',
    products=[
        {'id': 'prod_123'}
    ],
    external_id='EXT123',
    deliver_at='2025-01-01T00:00:00Z',
    custom_fields={
        'survey_id': '123'
    },
    language='en',
    delivery_method={
        'method': 'email'
    },
    meta_data={
        'key': 'value'
    }
)

# Approve Order
tremendous.orders.approve(id='ABCD123')

# Reject Order
tremendous.orders.reject(id='ABCD123')
```

#### Products

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Products
tremendous.products.list(country='US', currency='USD', subcategory='')

# Get Product
tremendous.products.get(product_id='PROD123')
```

#### Campaigns

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Campaigns
tremendous.campaigns.list()

# Get Campaign
tremendous.campaigns.get(campaign_id='CAMP123')

# Create Campaign
tremendous.campaigns.create(
    name='My Campaign',
    description='Example',
    products=['PROD1', 'PROD2'],
    webpage_style={'headline': 'Hello'},
    email_style={'sender_name': 'Sender'}
)

# Update Campaign
tremendous.campaigns.update(
    id='CAMP123',
    name='Updated',
    description='Updated description',
    products=['PROD1'],
    webpage_style={'headline': 'Hi'},
    email_style={'subject_line': 'Subject'}
)
```

#### Funding Sources

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Funding Sources
tremendous.funding_sources.list()

# Get Funding Source
tremendous.funding_sources.get(id='FS123')
```

#### Invoices

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# Get Invoice
tremendous.invoices.get(id='INV123')

# List Invoices
tremendous.invoices.list(offset=0, limit=10)

# Create Invoice
tremendous.invoices.create(amount=1000.0, po_number='PO-123', memo='Test')

# Delete Invoice
tremendous.invoices.delete(id='INV123')
```

#### Topups

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Topups
tremendous.topups.list(offset=0)

# Get Topup
tremendous.topups.get(id='TOP123')

# Create Topup
tremendous.topups.create(
    amount=500.0, 
    idempotency_key='unique-key-123', 
    funding_source_id='FS123'
)
```

#### Balance Transactions

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Balance Transactions
tremendous.balance_transactions.list(
    offset=0, 
    limit=10, 
    created_at_gte='2024-01-01', 
    created_at_lte='2024-12-31'
)
```

#### Organizations

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Organizations
tremendous.organizations.list()

# Get Organization
tremendous.organizations.get(id='ORG123')

# Create Organization
tremendous.organizations.create(
    name='Acme Inc', 
    website='https://acme.example', 
    with_api_key=False, 
    copy_settings=None, 
    phone='+123456789'
)

# Create API Key
tremendous.organizations.create_api_key()
```

#### Members

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Members
tremendous.members.list()

# Get Member
tremendous.members.get(id='MEM123')

# Create Member
tremendous.members.create(email='user@example.com', role='admin')
```

#### Roles

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Roles
tremendous.roles.list()
```

#### Fields

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Fields
tremendous.fields.list()
```

#### Webhooks

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Webhooks
tremendous.webhooks.list()

# Get Webhook
tremendous.webhooks.get(id='WH123')

# Create Webhook
tremendous.webhooks.create(url='https://your-app.example/webhooks/tremendous')

# Delete Webhook
tremendous.webhooks.delete(id='WH123')

# Test Webhook
tremendous.webhooks.test_webhook(id='WH123', event='reward.sent')

# List Webhook Events
tremendous.webhooks.list_events(id='WH123')
```

#### Forex

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

# List Forex Rates
tremendous.forex.list(base='USD')
```

### License

This project is licensed under the terms of the license found in `LICENSE`.

