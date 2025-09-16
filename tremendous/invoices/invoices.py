from pydantic import BaseModel
from typing import List, Dict, TYPE_CHECKING, Optional
from tremendous.rewards.reward import RewardModel
from tremendous.orders.order import OrderModel

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class InvoiceModel(BaseModel):
    id: str
    po_number: Optional[str] = None
    amount: Optional[float] = None
    international: Optional[bool] = None
    status: Optional[str] = None
    orders: Optional[List[OrderModel]] = None
    rewards: Optional[List[RewardModel]] = None
    created_at: Optional[str] = None
    paid_at: Optional[str] = None

class Invoices:

    def __init__(self, client: "Tremendous"):
        self.client = client

    def get(self, id: str) -> InvoiceModel:
        """
        Retrieve an invoice.
        
        Args:
            id (str): The ID of the invoice.
        """
        return self.client._fetch(
            path=f"/invoices/{id}",
            model_cls=InvoiceModel,
            list_key="invoice"
        )
    
    def list(self, offset: int = 0, limit: int = 10) -> List[InvoiceModel]:
        """
        Retrieve a list of invoices.

        Args:
            offset (int, optional): Offsets the returned list by the given number of invoices. The returned invoices are ordered (and offsetted) by their creation date (DESC).
            limit (int, optional): Limits the number of invoices returned.
        """

        return self.client._fetch_list(
            path="/invoices",
            model_cls=InvoiceModel,
            list_key="invoices",
            params={
                "offset": offset,
                "limit": limit
            }
        )

    def create(self, amount: float, po_number: str, memo: str) -> InvoiceModel:
        """
        Create an invoice.
        
        Args:
            amount (float): The amount of the invoice.
            po_number (str): The PO number of the invoice.
            memo (str): The memo of the invoice.
        """
        return self.client._create(
            path="/invoices",
            model_cls=InvoiceModel,
            params={
                "amount": amount,
                "po_number": po_number,
                "memo": memo
            },
            list_key="invoice"
        )

    def delete(self, id: str) -> InvoiceModel:
        """
        Delete an invoice.
        
        Args:
            id (str): The ID of the invoice.
        """
        return self.client._delete(
            path=f"/invoices/{id}",
            model_cls=InvoiceModel,
            list_key="invoice",
            params={
                "id": id
            }
        )
