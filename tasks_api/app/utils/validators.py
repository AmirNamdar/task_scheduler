from urllib.parse import urlparse
from uuid import UUID


class DataValidator:
    @staticmethod
    def is_valid_uuid(uuid_to_test, version=4) -> bool:
        """
        Check if uuid_to_test is a valid UUID.
        """
        try:
            uuid_obj = UUID(uuid_to_test, version=version)
        except ValueError:
            return False

        return str(uuid_obj) == uuid_to_test

    @staticmethod
    def is_valid_url(url: str):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
