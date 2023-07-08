from typing import Any

from api_layer.responses.base_responses import BaseResponse


class APIDocsUtils:
    @staticmethod
    def get_content_response_desc(data: Any) -> dict[str, dict[str, Any]]:
        return {
            "content": {
                "application/json": {
                    "example": data,
                },
            }
        }

    @classmethod
    def get_responses_dict(
        cls, responses: list[BaseResponse]
    ) -> dict[int, dict[str, dict[str, Any]]]:
        return {
            res.status_code: cls.get_content_response_desc(res.dict())
            for res in responses
        }
