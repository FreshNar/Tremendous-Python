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

    A reward is a monetary incentive sent to an individual recipient.

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
    A reward is a monetary incentive sent to an individual recipient.
    Rewards have an amount, a delivery method, and a set of redemption choices available to the recipient.

    [Tremendous Rewards API Reference](https://developers.tremendous.com/reference/rewards)
    """

    def __init__(self, client: "Tremendous"):
        self.client = client

    def get(self, id: str) -> RewardModel:
        """
        Retrieve a reward by its ID.
        
        Args:
            id (str): The ID of the reward.

        Returns:
            RewardModel: The reward.

        ```python
        tremendous.Rewards.get("1234567890")
        ```
        """

        return self.client._fetch(
            path=f"/rewards/{id}",
            model_cls=RewardModel,
            list_key="reward"
        )

    def list(self, offset: int = 0, limit: int = 100) -> List[RewardModel]:
        """
        Retrieve a list of rewards.

        Args:
            offset (int, optional): Offsets and orders by their creation date.
            limit (int, optional): Limits the number of rewards returned.

        Returns:
            RewardModel: The list of rewards.

        ```python
        tremendous.Rewards.list()
        ```
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
        Generate a redemption link for the reward identified by the id.

        Args:
            id (str): The ID of the reward.

        Returns:
            URL: The redemption link.

        ```python
        tremendous.Rewards.generate_reward_url("1234567890")
        ```
        """

        return self.client._create(
            path=f"/rewards/{id}/generate_link",
            params={
                "id": id
            }
        )

    def resend_reward(self, id: str, updated_email: str = None, updated_phone: str = None) -> RewardModel:
        """
        Resends a reward, identified by the given id, to its recipient. Only rewards with a previous delivery failure can be resent.

        Args:
            id (str): The ID of the reward.
            updated_email (str, optional): The email address to send the reward to.
            updated_phone (str, optional): The phone number to send the reward to.

        Returns:
            RewardModel: The reward.

        ```python
        tremendous.Rewards.resend_reward("1234567890", updated_email="test@test.com", updated_phone="1234567890")
        ```
        """

        return self.client._create(
            path=f"/rewards/{id}/resend",
            params={
                "id": id,
                "updated_email": updated_email,
                "updated_phone": updated_phone
            }
        )

    def cancel_reward(self, id: str) -> RewardModel:
        """
        Cancels a reward, identified by the given id.

        Args:
            id (str): The ID of the reward.

        Returns:
            RewardModel: The reward.

        ```python
        tremendous.Rewards.cancel_reward("1234567890")
        ```
        """

        return self.client._create(
            path=f"/rewards/{id}/cancel",
            params={
                "id": id
            }
        )