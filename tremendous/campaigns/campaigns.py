from pydantic import BaseModel
from typing import List, TYPE_CHECKING, Optional, Dict

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class WebpageStyleModel(BaseModel):
    headline: Optional[str] = None
    message: Optional[str] = None
    logo_image_url: Optional[str] = None
    logo_image_height_px: Optional[int] = None
    logo_background_color: Optional[str] = None
    background_color: Optional[str] = None

class EmailStyleModel(BaseModel):
    sender_name: Optional[str] = None
    subject_line: Optional[str] = None
    logo_image_url: Optional[str] = None
    logo_image_height_px: Optional[int] = None
    logo_background_color: Optional[str] = None
    button_color: Optional[str] = None

class CampaignModel(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    products: Optional[List[str]] = None
    webpage_style: Optional[WebpageStyleModel] = None
    email_style: Optional[EmailStyleModel] = None

class Campaigns:

    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self) -> List[CampaignModel]:
        return self.client._fetch_list(
            path="/campaigns",
            model_cls=CampaignModel,
            list_key="campaigns"
        )

    def get(self, campaign_id: str) -> CampaignModel:
        return self.client._fetch(
            path=f"/campaigns/{campaign_id}",
            model_cls=CampaignModel,
            list_key="campaign"
        )
    
    def create(self, name: str, description: str, products: List[str], webpage_style: Optional[WebpageStyleModel] = None, email_style: Optional[EmailStyleModel] = None) -> CampaignModel:
        return self.client._create(
            path="/campaigns",
            model_cls=CampaignModel,
            params={"name": name, "description": description, "products": products, "webpage_style": webpage_style, "email_style": email_style},
            list_key="campaign"
        )
    
    def update(
        self, 
        id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        products: Optional[List[str]] = None,
        webpage_style: Optional[Dict] = None,
        email_style: Optional[Dict] = None
    ) -> CampaignModel:
        return self.client._update(
            path=f"/campaigns/{id}",
            model_cls=CampaignModel,
            params={
                "name": name, 
                "description": description, 
                "products": products, 
                "webpage_style": webpage_style, 
                "email_style": email_style
            },
            list_key="campaign"
        )
    