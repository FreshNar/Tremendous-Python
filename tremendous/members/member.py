from pydantic import BaseModel
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class MemberModel(BaseModel):
    id: str
    email: Optional[str] = None
    name: Optional[str] = None
    active: Optional[bool] = None
    role: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    last_login_at: Optional[str] = None

class Members:

    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self) -> List[MemberModel]:
        """
        Retrieve a list of members.
        
        Returns:
            List[MemberModel]: A list of member objects.
        """
        return self.client._fetch_list(
            path="/members",
            model_cls=MemberModel,
            list_key="members"
        )
        
    def get(self, id: str) -> MemberModel:
        """
        Retrieve a member.
        
        Args:
            id (str): The ID of the member.

        Returns:
            MemberModel: The member object.
        """
        return self.client._fetch(
            path=f"/members/{id}",
            model_cls=MemberModel,
            list_key="member"
        )

    def create(self, email: str, role: str) -> MemberModel:
        """
        Create a member.
        
        Args:
            email (str): The email of the member.
            role (str): The role of the member.

        Returns:
            MemberModel: The created member object.
        """
        return self.client._create(
            path="/members",
            model_cls=MemberModel,
            params={"email": email, "role": role},
            list_key="member"
        )