### Quickstart
After you have your Tremendous API Key, initialize the client.

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="<your-api-key>", sandbox=True)
```

With your client initalized, you can start handling business. To introduce how the client interacts with the API, let's go through an example.

### Example Usage: Survey Participants get a Starbucks Gift Card

Let's say we want to programmatically reward our survey participants with a gift card to Starbucks. We have a few steps we need to take to make this happen.

1. We'll need to find the Id of the Starbucks gift card in the [Tremendous Catalog](https://www.tremendous.com/catalog-csv) .
2. Create an email Campaign template.
3. Finally, email the participant their gift card!

#### 1. Get the Starbucks Gift Card Id

To start, it might be useful to get information about our Starbucks Gift Card.

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

starbucks_gift_card = tremendous.Products.get(
    id="2XG0FLQXBDCZ"
)

# Pretty print the gift card data
print(starbucks_gift_card.model_dump_json(indent=4))
```
!!! info "Tip!"
    You can find the latest Tremendous Gift Card Catalog (including Id's) here: [Download CSV](https://www.tremendous.com/catalog-csv) 

By default, our client returns Objects, but we can turn that into JSON for better readability using the handy "model_dump_json" method.

```json
{
    "id": "2XG0FLQXBDCZ",
    "name": "Starbucks US",
    "description": "",
    "category": "merchant_card",
    "subcategory": "food_and_drink",
    "disclosure": "There are a small number of stores which are not wholly company owned and are not able to accept Starbucks Cards. These include concessions located within leisure facilities such as Centre Parcs, Village Hotels, Bourne Leisure and a number of our university stores. Please refer to our store locator (using the ‘Accept Starbucks Cards’ filter) for further information. Full terms can be found here: [www.starbucks.com/rewards/terms](https://www.starbucks.com/rewards/terms)",
    "skus": [
        {
            "min": 5.0,
            "max": 500.0
        }
    ],
    "currency_codes": [
        "USD"
    ],
    "countries": [
        {
            "abbr": "PR"
        },
        {
            "abbr": "US"
        }
    ],
    "images": [
        {
            "src": "https://testflight.tremendous.com/product_images/2XG0FLQXBDCZ/card",
            "type": "card",
            "content_type": "image/png"
        },
        {
            "src": "https://testflight.tremendous.com/product_images/2XG0FLQXBDCZ/logo",
            "type": "logo",
            "content_type": "image/png"
        }
    ],
    "usage_instructions": "**Starbucks eGift Redemption Instructions:**\r\n\r\n* Add to your Starbucks Rewards account [online](http://www.starbucks.com/rewards)\r\n* Or open the eGift on your device, and print or scan the barcode on your phone to pay at participating Starbucks stores\r\n* Join Starbucks Rewards via the Starbucks app on your mobile device and add your eGift via the instructions\r\n* Visit the [Starbucks Store Locator](http://www.starbucks.com/store-locator?map=39.635307,-101.337891,5z) to find the nearest store \r\n* For our full Terms & Conditions,[ click here](http://www.starbucks.com/terms/manage-Terms & Conditions,[ click here](http://www.starbucks.com/terms/manage-gift-cards/) ",
    "documents": null
}
```

There's alot of information about our gift card here. What we'll note is that our minimum gift card amount is <b> $5 USD </b> — seen in "skus".

#### 2. Create an Email Template for our participants

Now that we have information about our gift card. Let's design and write some copy for our email Campaign. 

This is particularly useful, becuase we don't need to create a new email template everytime we want to send a gift card for this Campaign.

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

campaign = tremendous.Campaigns.create(
    name="Thank survey participants",
    description="A starbucks gift card as a thank you to survery participants",
    products=[starbucks_gift_card.id],
    webpage_style={
        "headline": "Thank you for your participation", 
        "message": "We're rewarding you with a Starbucks Gift Card!", 
        "logo_background_color": "#121212", 
        "background_color": "#121212"
    },
    email_style={
        "sender_name": "John Marketer",
        "subject_line": "Thank you for being a participant!",
        "logo_background_color": "#121212",
        "button_color": "#121212"
    }
)
```

The create method will return the Campaign Object. We'll need the "id" of the Campaign if we want to reuse it in the future.

```python
campaign.id

```

#### 3. Create an Order and send our gift card via email

```python
from tremendous import TremendousClient

tremendous = TremendousClient(api_key="TestTEST_aB....", sandbox=True)

order = tremendous.Orders.create(
    payment_funding_source_id="balance", 
    campaign_id=campaign.id, 
    value={
        "denomination": 5, 
        "currency_code": "USD"
    }, 
    recipient={
        "name": "Jake Smith", 
        "email": "jsmith@example.com"
    }, 
    language="en",
    delivery_method={"method": "email"},
)

```

Great! Now Jake Smith received his gift card and we didn't have to take a trip to Starbucks to make it happen.