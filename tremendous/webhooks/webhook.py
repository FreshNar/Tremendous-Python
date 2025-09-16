import requests
from pydantic import BaseModel
from typing import Optional, TYPE_CHECKING, List

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class EventModel(BaseModel):
    events: List[str]

class WebhookModel(BaseModel):
    id: str
    url: Optional[str] = None
    private_key: Optional[str] = None

class Webhooks:
    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self) -> List[WebhookModel]:
        """
        Retrieve a list of webhooks.
        """
        return self.client._fetch_list(
            path="/webhooks",
            model_cls=WebhookModel,
            list_key="webhooks"
        )

    def get(self, id: str) -> WebhookModel:
        """
        Retrieve a webhook.
        """
        return self.client._fetch(
            path=f"/webhooks/{id}",
            model_cls=WebhookModel,
            list_key="webhook"
        )
    
    def create(self, url: str) -> WebhookModel:
        """
        Create a webhook.
        """
        return self.client._create(
            path="/webhooks",
            model_cls=WebhookModel,
            params={"url": url},
            list_key="webhook"
        )

    def delete(self, id: str) -> WebhookModel:
        """
        Delete a webhook.
        """
        return self.client._delete(
            path=f"/webhooks/{id}",
            model_cls=WebhookModel,
            list_key="webhook"
        )

    def test_webhook(self, id: str, event: str) -> WebhookModel:
        """
        Making a request to this endpoint will cause our system to trigger a webhook for the specified event. Tremendous webhooks guide: https://developers.tremendous.com/docs/webhooks-1

        Args:
            id (str): The ID of the webhook.
            event (str): The event to test the webhook for.

        Returns:
            WebhookModel: The webhook object.
        """

        url = f"{self.client.base_url}/webhooks/{id}/simulate"

        payload = {
            "event": event
        }

        headers = {
            "accept" : "text/html",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.client.api_key}"
        }
        response = requests.post(url, headers=headers, json=payload)
        
        return response

    def list_events(self, id: str) -> List[str]:
        """
        List all events that can be used to test a webhook.

        Args:
            id (str): The ID of the webhook.

        Returns:
            EventModel: A list of events.
        """
        return self.client._fetch_list(
            path=f"/webhooks/{id}/events",
            model_cls=EventModel,
            list_key=None
        )