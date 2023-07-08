import json
import traceback
from typing import Any, Dict, Optional

from fastapi.responses import JSONResponse


class BaseResponse(JSONResponse):
    def __init__(self, data: Dict, status_code: int, success: bool):
        self.content = {
            "success": success,
            "data": data,
        }
        super().__init__(
            status_code=status_code,
            content=self.content,
        )

    def dict(self, *args, **kwargs):
        return json.loads(self.render(self.content))


class SuccessResponse(BaseResponse):
    def __init__(self, data: Optional[Dict] = None, status_code: int = 200):
        super().__init__(
            data=data or {},
            status_code=status_code,
            success=True,
        )


class ErrorResponse(BaseResponse):
    def __init__(
        self,
        message: str,
        status_code: int = 500,
        exception: Optional[Exception] = None,
        **kwargs: Any,
    ):
        exception_log = {
            "exception": repr(exception),
            "traceback": traceback.format_exc(),
        }
        error_code = getattr(exception, "error_code", None)

        super().__init__(
            data={
                **kwargs,
                **exception_log,
                "message": message,
                "error_code": error_code or "UNEXPECTED_ERROR",
            },
            status_code=status_code,
            success=False,
        )


def get_unexpected_error_response(
    exception: Optional[Exception] = None,
) -> ErrorResponse:
    return ErrorResponse(
        message="Oops, something went wrong",
        exception=exception,
    )
