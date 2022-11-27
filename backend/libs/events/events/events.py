import requests


class SchoolClassEventHandler:
    # TODO: Make it a variable.
    uri = "http://schoolclass:8082"

    @classmethod
    def get(cls, class_id: int, **kwargs) -> bool:
        url = f"{cls.uri}/classes/{class_id}"
        return requests.get(url).ok
