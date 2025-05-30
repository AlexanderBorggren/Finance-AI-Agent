from enum import Enum

class ApiSource(Enum):
    FINNHUB = {
        "label": "finnhub",
        "handler_module": "api.sources.finnhub",
        "base_url": None,
        "use_sdk": True
    }
    MOCK = {
        "label": "mock",
        "handler_module": "api.sources.mock",
        "base_url": None,
        "use_sdk": False
    }


    @property
    def label(self) -> str:
        return self.value["label"]
    @property
    def handler(self) -> str:
        return self.value["handler_module"]
    @property
    def base_url(self) -> str | None:
        return self.value["base_url"]
    @property
    def use_sdk(self) -> str:
        return self.value["use_sdk"]