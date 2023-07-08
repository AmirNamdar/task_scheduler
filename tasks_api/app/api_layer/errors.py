from utils.base_error import BaseError
from fastapi.responses import JSONResponse


class APILayerError(BaseError, JSONResponse):
    pass
