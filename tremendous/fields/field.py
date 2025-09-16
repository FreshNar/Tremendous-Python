from pydantic import BaseModel
from typing import List, TYPE_CHECKING, Optional, Dict

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class FieldModel(BaseModel):
    id: str
    label: Optional[str] = None
    data_type: Optional[str] = None
    data: Optional[Dict] = None
    required: Optional[bool] = None
    scope: Optional[str] = None

class Fields:

    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self) -> List[FieldModel]:
        """
        Retrieve a list of fields.

        For reporting and analytics purposes, custom fields can be associated with rewards 
        generated through the API. Custom fields must be first added by members of your 
        admin team through the Tremendous Dashboard.

        Returns:
            List[FieldModel]: A list of field objects.
        """
        return self.client._fetch_list(
            path="/fields",
            model_cls=FieldModel,
            list_key="fields"
        )
        
        