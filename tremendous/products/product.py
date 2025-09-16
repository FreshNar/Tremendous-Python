from pydantic import BaseModel
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class SkuModel(BaseModel):
    min: float = None
    max: float = None

class CountryModel(BaseModel):
    abbr: str

class ImageModel(BaseModel):
    src: str = None
    type: str = None
    content_type: str = None

class DocumentModel(BaseModel):
    cardholder_agreement_pdf: str = None
    cardholder_agreement_html: str = None
    privacy_policy_url: str = None

class ProductModel(BaseModel):
    """
    Represents a Tremendous product.
    
    A product represents a payout mechanism for a reward, such as gift cards,
    prepaid cards, or other incentives available through the Tremendous platform.
    
    Attributes:
        id (str): Unique identifier for the product.
        name (str): Display name of the product.
        description (str): Detailed description of the product.
        category (str): Main category the product belongs to.
        subcategory (str): Optional subcategory for more specific classification.
        disclosure (str): Terms and conditions or disclosure information.
        skus (List[Dict]): Available SKUs/variants for this product.
        currency_codes (List[str]): Supported currency codes (e.g., ['USD', 'EUR']).
        countries (List[Dict]): Countries where this product is available.
        images (List[Dict]): Product images and assets.
        usage_instructions (str): Instructions on how to use/redeem the product.
        documents (Dict): Additional documentation or terms.
    """
    id: str
    name: str
    description: str
    category: str
    subcategory: str = ""
    disclosure: str = ""
    skus: List[SkuModel]
    currency_codes: List[str]
    countries: List[CountryModel]
    images: List[ImageModel]
    usage_instructions: str = ""
    documents: DocumentModel = None

class Products:
    """
    Client for interacting with Tremendous products.
    
    A product represents a payout mechanism for a reward. This class provides
    methods to retrieve available products and get detailed information about
    specific products.
    
    Reference: https://docs.tremendous.com/reference/get_products
    
    Args:
        client (Tremendous): The main Tremendous client instance.
    """

    def __init__(self, client: "Tremendous"):
        """
        Initialize the Products client.
        
        Args:
            client (Tremendous): The main Tremendous client instance.
        """
        self.client = client

    def list(self, country: str = "US", currency: str = "USD", subcategory: str = "") -> List[ProductModel]:
        """
        Retrieve a list of available products.
        
        This method fetches all products available for the specified country,
        currency, and optionally filtered by subcategory.
        
        Args:
            country (str, optional): Country code (e.g., 'US', 'CA'). Defaults to 'US'.
            currency (str, optional): Currency code (e.g., 'USD', 'CAD'). Defaults to 'USD'.
            subcategory (str, optional): Filter by subcategory. Defaults to ''.
        
        Returns:
            List[ProductModel]: List of available products matching the criteria.
        
        Example:
            >>> products = client.products.list(country="US", currency="USD")
            >>> for product in products:
            ...     print(f"{product.name}: {product.description}")
        """
        return self.client._fetch_list(
            path="/products",
            model_cls=ProductModel,
            list_key="products",
            params={
                "country": country,
                "currency": currency,
                "subcategory": subcategory
            }
        )

    def get(self, product_id: str) -> ProductModel:
        """
        Retrieve detailed information about a specific product.
        
        Args:
            product_id (str): The unique identifier of the product.
        
        Returns:
            ProductModel: Detailed product information.
        
        Raises:
            requests.HTTPError: If the product is not found or request fails.
        
        Example:
            >>> product = client.products.get("product-123")
            >>> print(f"Product: {product.name}")
            >>> print(f"Available currencies: {product.currency_codes}")
        """
        return self.client._fetch(
            path=f"/products/{product_id}",
            model_cls=ProductModel,
            list_key='product'
        )
    