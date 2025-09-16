import requests

class Tremendous:
    """
    Main client for interacting with the Tremendous API.
    
    This client provides a Python interface to the Tremendous API, allowing you to
    manage products, rewards, and other Tremendous resources.
    
    Args:
        api_key (str): Your Tremendous API key. Get this from your Tremendous dashboard.
        sandbox (bool, optional): Whether to use the sandbox environment. 
                                 Defaults to False (production).
    
    Attributes:
        api_key (str): The API key used for authentication.
        base_url (str): The base URL for API requests.
        session (requests.Session): The HTTP session used for requests.
        products (Products): Instance of the Products API client.
    
    Example:
        >>> from tremendous import TremendousClient
        >>> client = TremendousClient(api_key="your-api-key", sandbox=True)
        >>> products = client.products.list()
    """

    def __init__(self, api_key: str, sandbox: bool = False):
        """
        Initialize the TremendousClient.
        
        Args:
            api_key (str): Your Tremendous API key.
            sandbox (bool, optional): Whether to use sandbox environment. Defaults to False.
        """
        self.api_key = api_key
        # Use correct base URLs; do not include resource paths
        self.base_url = (
            "https://api.tremendous.com/v2"
            if not sandbox
            else "https://testflight.tremendous.com/api/v2"
        )
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        })

        from tremendous.products import Products
        from tremendous.rewards import Rewards
        self.products = Products(self)
        self.rewards = Rewards(self)

    def _request(self, method: str, url: str, **kwargs) -> requests.Response:
        """
        Make a request to the Tremendous API.
        
        This is an internal method used by other API methods to make HTTP requests.
        It handles URL construction, authentication, and error handling.
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE, etc.).
            url (str): The endpoint URL (relative to base_url).
            **kwargs: Additional arguments passed to requests.Session.request().
        
        Returns:
            requests.Response: The HTTP response object.
            
        Raises:
            requests.HTTPError: If the request fails with a non-2xx status code.
        """
        url = f"{self.base_url}{url}"
        response = self.session.request(method, url, **kwargs)
        if not response.ok:
            raise requests.HTTPError(f"Request failed with status code {response.status_code}")
        return response

    def _fetch(
        self,
        path: str,
        model_cls,
        list_key: str,
        params: dict | None = None,
        method: str = "GET",
    ):
        """
        Fetch a resource from the API.
        
        Args:
            path: The path to the API endpoint.
            model_cls: The model class to use for the response.
            params: The parameters to pass to the API endpoint.
            method: The HTTP method to use for the request.
        """
        response = self._request(method, path, params=params)
        data = response.json()
        return model_cls(**data[list_key])

    def _fetch_list(
        self,
        path: str,
        model_cls,
        list_key: str,
        params: dict | None = None,
        method: str = "GET",
    ):
        """
        Fetch a list of resources from the API.
        
        Args:
            path: The path to the API endpoint.
            model_cls: The model class to use for the response.
            list_key: The key in the response JSON that contains the list of resources.
            params: The parameters to pass to the API endpoint.
            method: The HTTP method to use for the request.
        """
        response = self._request(method, path, params=params)
        data = response.json()
        print(data)
        return [model_cls(**item) for item in data[list_key]]
