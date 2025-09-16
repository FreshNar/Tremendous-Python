from pydantic import BaseModel
from typing import List, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from tremendous.client import Tremendous

class ForexModel(BaseModel):
    forex: Dict

class Forex:

    def __init__(self, client: "Tremendous"):
        self.client = client

    def list(self, base: str) -> ForexModel:
        """
        Retrieve a list of exchange rates

        Args:
            base (str): The base currency to get exchange rates for.

        Returns:
            ForexModel: A list of exchange rates.
        """
        return self.client._fetch_list(
            path="/forex",
            model_cls=ForexModel,
            params={
                "base": base
            }
        )