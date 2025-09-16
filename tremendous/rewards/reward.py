import json
from pydantic import BaseModel
from typing import List, TYPE_CHECKING
from tremendous.products.product import ProductModel

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class RewardURLModel(BaseModel):
    id: str
    url: str

class ValueModel(BaseModel):
    denomination: float
    currency_code: str

class RecipientModel(BaseModel):
    name: str
    email: str
    phone: str

class DeliveryModel(BaseModel):
    method: str
    status: str

class RewardModel(BaseModel):
    """
    Represents a tremendous reward.

    A reward is a monetary incentive sent to an individual recipient. They're probably what brought you to Tremendous.

    Attributes:
        id (str): Tremendous ID of the reward.
        order_id (str): Tremendous ID of the order this reward is part of.
        created_at (string): Date the reward was created.
        campaign_id (string): Tremendous ID of the campaign this reward is part of.
        products (list): List of products in the reward.
        value (float): Value of the reward.

    """
    id: str
    order_id: str
    created_at: str
    value: ValueModel
    delivery: DeliveryModel
    recipient: RecipientModel
    campaign_id: str = ""
    products: List[ProductModel] = []

class Rewards:

    """
    Client for interacting with Tremendous rewards. 

    """

    def __init__(self, client: "Tremendous"):
        self.client = client

    def get(self, id: str) -> RewardModel:
        return self.client._fetch(
            path=f"/rewards/{id}",
            model_cls=RewardModel,
            list_key="reward"
        )

    def list(self, offset: int = 0, limit: int = 100) -> List[RewardModel]:
        """
        Retrieve a list of rewards.

        Args:
            offset (int, optional): Offsets the returned list by the given number of rewards. The returned rewards are ordered (and offsetted) by their creation date (DESC).
            limit (int, optional): Limits the number of rewards returned.

        """

        return self.client._fetch_list(
            path="/rewards",
            model_cls=RewardModel,
            list_key="rewards",
            params={
            "offset": offset,
            "limit": limit
            }
        )

    def generate_reward_url(self, id: str) -> str:
        """
        Generate a redemption link for the reward identified by the id in the URL.

        Args:
            id (str): The ID of the reward.
        """

        return self.client._create(
            path=f"/rewards/{id}/generate_link",
            params={
                "id": id
            }
        )

    def resend_reward(self, id: str, updated_email: str = None, updated_phone: str = None):
        """
        Resends a reward, identified by the given id in the URL, to its recipient. Only rewards with a previous delivery failure can be resent.

        Args:
            id (str): The ID of the reward.
            updated_email (str, optional): The email address to send the reward to.
            updated_phone (str, optional): The phone number to send the reward to.
        """

        return self.client._create(
            path=f"/rewards/{id}/resend",
            params={
                "id": id,
                "updated_email": updated_email,
                "updated_phone": updated_phone
            }
        )

    def cancel_reward(self, id: str):
        """
        Cancels a reward, identified by the given id in the URL.

        Args:
            id (str): The ID of the reward.
        """

        return self.client._create(
            path=f"/rewards/{id}/cancel",
            params={
                "id": id
            }
        )