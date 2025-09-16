from pydantic import BaseModel
from typing import Optional, TYPE_CHECKING, List

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class RoleModel(BaseModel):
    id: str
    title: Optional[str] = None
    description: Optional[str] = None

class Roles:
    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self) -> List[RoleModel]:
        """
        Retrieve a list of roles.
        Args:
            None

        Returns:
            List[RoleModel]: A list of role objects.
        """
        return self.client._fetch_list(
            path="/roles",
            model_cls=RoleModel,
            list_key="roles"
        )
