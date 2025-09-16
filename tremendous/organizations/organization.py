from pydantic import BaseModel
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class OrganizationModel(BaseModel):
    id: str
    name: Optional[str] = None
    website: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None

class Organizations:

    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self) -> List[OrganizationModel]:
        """
        Retrieve a list of organizations.
        
        Returns:
            List[OrganizationModel]: A list of organization objects.
        """
        return self.client._fetch_list(
            path="/organizations",
            model_cls=OrganizationModel,
            list_key="organizations"
        )

    def get(self, id: str) -> OrganizationModel:
        """
        Retrieve an organization by ID.
        
        Args:
            id (str): The ID of the organization to retrieve.
            
        Returns:
            OrganizationModel: The organization object.
        """
        return self.client._fetch(
            path=f"/organizations/{id}",
            model_cls=OrganizationModel,
            list_key="organization"
        )
    
    def create(self, name: str, website: str, with_api_key: bool = False, copy_settings: str = None, phone: str = None) -> OrganizationModel:
        """
        Create a new organization.
        
        Args:
            name (str): The name of the organization.
            website (str): The website URL of the organization.
            with_api_key (bool, optional): Whether to create an API key for the organization.
            copy_settings (str, optional): A list of the settings that you wish to copy over to the new organization. See: https://developers.tremendous.com/reference/create-organization
            phone (str, optional): The phone number of the organization.
            
        Returns:
            OrganizationModel: The created organization object.
        """
        return self.client._create(
            path="/organizations",
            model_cls=OrganizationModel,
            params={"name": name, "website": website, "with_api_key": with_api_key, "copy_settings": copy_settings, "phone": phone},
            list_key="organization"
        )

    def create_api_key(self) -> OrganizationModel:
        """
        Create an API key for an organization.
        
        Args:
            None
        """
        return self.client._create(
            path=f"/organizations/create_api_key",
            model_cls=None,
            list_key=None
        )
        