from pydantic import BaseModel
from typing import List, Dict, TYPE_CHECKING, Optional
from tremendous.products.product import ProductModel

if TYPE_CHECKING:
    from tremendous.client import Tremendous

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

    def get(self, reward_id: str) -> RewardModel:
        return self.client._fetch(
            path=f"/rewards/{reward_id}",
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