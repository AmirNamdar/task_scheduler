from typing import Optional
from utils.base_error import BaseError


# Base errors
class DBLayerError(BaseError):
    def __init__(self, message: str):
        super().__init__(message)
