### Usage Examples

List recent orders

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

orders = tremendous.Orders.list(limit=5)
for order in orders:
    print(order.id, order.status, order.rewards)
```

Create a simple order (email delivery)

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

order = tremendous.Orders.create(
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

Update an existing campaign

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

campaign = tremendous.Campaigns.update(
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