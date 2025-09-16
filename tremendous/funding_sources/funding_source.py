from pydantic import BaseModel
from typing import List, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class FundingSourceModel(BaseModel):
    id: str
    method: Optional[str] = None
    usage_permissions: List[str]
    status: Optional[str] = None
    type: Optional[str] = None
    meta: Optional[Dict] = None

class FundingSources:
    """
    Funding sources represent different ways to pay for orders.

    """

    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self) -> List[FundingSourceModel]:
        """
        Retrieve a list of funding sources.
        
        """
        return self.client._fetch_list(
            path="/funding_sources",
            model_cls=FundingSourceModel,
            list_key="funding_sources"
        )

    def get(self, id: str) -> FundingSourceModel:
        """
        Retrieve a funding source.
        
        Args:
            id (str): The ID of the funding source.
        """
        return self.client._fetch(
            path=f"/funding_sources/{id}",
            model_cls=FundingSourceModel,
            list_key="funding_source"
        )