from pydantic import BaseModel
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class TopupModel(BaseModel):
    id: str
    amount: Optional[float] = None
    processing_fee: Optional[float] = None
    funding_source_id: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    fully_credited_at: Optional[str] = None
    rejected_at: Optional[str] = None
    reversed_at: Optional[str] = None
    reversed_reason: Optional[str] = None
    idempotency_key: Optional[str] = None

class Topups:

    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self, offset: int = 0) -> List[TopupModel]:
        """
        Retrieve a list of topups.

        Args:
            offset (int, optional): Offsets the returned list by the given number of topups. The returned topups are ordered (and offsetted) by their creation date (DESC).
        """
        return self.client._fetch_list(
            path="/topups",
            model_cls=TopupModel,
            list_key="topups",
            params={
                "offset": offset
            }
        )
        
    def get(self, id: str) -> TopupModel:
        """
        Retrieve a topup.
        """
        return self.client._fetch(
            path=f"/topups/{id}",
            model_cls=TopupModel,
            list_key="topup"
        )
        
    def create(self, amount: float, idempotency_key: str, funding_source_id: str) -> TopupModel:
        """
        Create a topup.

        Args:
            amount (float): The amount of the topup.
            idempotency_key (str): The idempotency key of the topup.
            funding_source_id (str): The funding source ID of the topup.
        """
        return self.client._create(
            path="/topups",
            model_cls=TopupModel,
            params={
                "amount": amount,
                "idempotency_key": idempotency_key,
                "funding_source_id": funding_source_id
            },
            list_key="topup"
        )
        
        