from pydantic import BaseModel
from typing import List, Dict, TYPE_CHECKING, Optional
from tremendous.rewards.reward import RewardModel

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class RefundModel(BaseModel):
    total: Optional[float] = None

class PaymentModel(BaseModel):
    subtotal: Optional[float] = None
    total: Optional[float] = None
    fees: Optional[float] = None
    discount: Optional[float] = None
    refund: Optional[RefundModel] = None

class OrderModel(BaseModel):
    id: Optional[str] = None    
    external_id: Optional[str] = None
    campaign_id: Optional[str] = None
    created_at: Optional[str] = None
    status: Optional[str] = None
    channel: Optional[str] = None
    payment: Optional[PaymentModel] = None
    invoice_id: Optional[str] = None
    rewards: Optional[List[RewardModel]] = None

class Orders:

    def __init__(self, client: "Tremendous"):
        self.client = client

    def get(self, order_id: str) -> OrderModel:
        return self.client._fetch(
            path=f"/orders/{order_id}",
            model_cls=OrderModel,
            list_key="order"
        )

    def list(
            self, 
            offset: int = 0, 
            campaign_id: str = None, 
            external_id: str = None, 
            created_at_gte: str = None, 
            created_at_lte: str = None, 
            limit: int = 10) -> List[OrderModel]:
        
        """
        Retrieve a list of orders.

        Args:
            offset (int, optional): Offsets the returned list by the given number of orders. The returned orders are ordered (and offsetted) by their creation date (DESC).
            campaign_id (str, optional): Filter by campaign ID.
            external_id (str, optional): Filter by external ID.
            created_at_gte (str, optional): Filter by created at greater than or equal to.
            created_at_lte (str, optional): Filter by created at less than or equal to.
            limit (int, optional): Limits the number of orders returned.
        """

        return self.client._fetch_list(
            path="/orders",
            model_cls=OrderModel,
            list_key="orders",
            params={
                "offset": offset,
                "campaign_id": campaign_id,
                "external_id": external_id,
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte,
                "limit": limit
            }
        )
    
    def create(
            self, 
            payment_funding_source_id: str,
            recipient: Dict, 
            value: Dict, 
            campaign_id: Optional[str] = None, 
            products: Optional[List[Dict]] = None, 
            external_id: Optional[str] = None, 
            deliver_at: str = None, 
            custom_fields: Dict[str, str] = None, 
            language: str = "en", 
            delivery_method: Dict = None, 
            meta_data: Dict[str, str] = None
        ) -> OrderModel:
        """
        Create an order.

        Args:
            external_id (str): The external ID of the order.
            payment_funding_source_id (str): The payment funding source ID of the order.
            products (List[Dict]): The products of the order.
            value (Dict): The value of the order.
            recipient (Dict): The recipient of the order.
            deliver_at (str, optional): The deliver at of the order.
            custom_fields (Dict[str, str], optional): The custom fields of the order.
            language (str, optional): The language of the order.
            delivery_method (Dict, optional): The delivery method of the order.
        """ 

        return self.client._create(
            path="/orders",
            model_cls=OrderModel,
            params={
                "external_id": external_id,
                "payment": {
                    "funding_source_id": payment_funding_source_id
                },
                "reward": {
                    "campaign_id": campaign_id,
                    "products": products,
                    "recipient": recipient,
                    "value": value,
                    "deliver_at": deliver_at,
                    "custom_fields": custom_fields,
                    "language": language,
                    "delivery": delivery_method,
                    "meta_data": meta_data
                },
            },
            list_key="order"
        )

    def approve(self, id: str) -> OrderModel:
        """
        Approves an order that is pending review, identified by the given id in the URL.

        Approvals is a feature that requires orders to be approved by an organization admin 
        before they are sent out. To enable approvals for your organization, please enable 
        'Allow approvals via API' via the organization's 'Order Approvals' settings from 
        the Tremendous dashboard.

        Args:
            id (str): The ID of the order.
        """

        return self.client._create(
            path=f"/order_approvals/{id}/approve",
            model_cls=OrderModel,   
            params={
                "id": id
            },
            list_key="order"
        )

    def reject(self, id: str) -> OrderModel:
        """
        Rejects an order that is pending review, identified by the given id in the URL.

        Args:
            id (str): The ID of the order.
        """

        return self.client._create(
            path=f"/order_approvals/{id}/reject",
            model_cls=OrderModel,
            params={
                "id": id
            },
            list_key="order"
        )
