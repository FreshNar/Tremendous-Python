from pydantic import BaseModel
from typing import List, TYPE_CHECKING, Optional
from tremendous.orders.order import OrderModel

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class BalanceTransactionModel(BaseModel):
    created_at: Optional[str] = None
    amount: Optional[float] = None
    balance: Optional[float] = None
    action: Optional[str] = None
    description: Optional[str] = None
    order: Optional[OrderModel] = None

class BalanceTransactions:

    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self, offset: int=0, limit: int=10, created_at_gte: str=None, created_at_lte: str=None) -> List[BalanceTransactionModel]:
        """
        Retrieve a list of balance transactions.
        
        Args:
            offset (int, optional): Offsets the returned list by the given number of balance transactions. The returned balance transactions are ordered (and offsetted) by their creation date (DESC).
            limit (int, optional): Limits the number of balance transactions returned.
            created_at_gte (str, optional): Filter by created at greater than or equal to.
            created_at_lte (str, optional): Filter by created at less than or equal to.
        """
        return self.client._fetch_list(
            path="/balance_transactions",
            model_cls=BalanceTransactionModel,
            list_key="transactions",
            params={
                "offset": offset,
                "limit": limit,
                "created_at[gte]": created_at_gte,
                "created_at[lte]": created_at_lte
            }
        )