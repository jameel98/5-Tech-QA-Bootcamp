import json
from jsonschema import validate, ValidationError


class Deck:
    def __init__(self):
        self._success: bool = False
        self._deck_id: str = ''
        self._shuffled: bool = False
        self._remaining: int = 0

    @property
    def success(self) -> bool:
        return self._success

    @success.setter
    def success(self, value: bool):
        self._success = value

    @property
    def deck_id(self) -> str:
        return self._deck_id

    @deck_id.setter
    def deck_id(self, value: str):
        self._deck_id = value

    @property
    def shuffled(self) -> bool:
        return self._shuffled

    @shuffled.setter
    def shuffled(self, value: bool):
        self._shuffled = value

    @property
    def remaining(self) -> int:
        return self._remaining

    @remaining.setter
    def remaining(self, value: int):
        self._remaining = value

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    def validate_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "_success": {"type": "boolean"},
                "_deck_id": {"type": "string"},
                "_shuffled": {"type": "boolean"},
                "_remaining": {"type": "integer"}
            },
            "required": ["_success", "_deck_id", "_shuffled", "_remaining"]
        }
        try:
            validate(instance=self.__dict__, schema=schema)
            print("JSON schema validation succeeded.")
        except ValidationError as e:
            print(f"JSON schema validation failed: {e.message}")
            raise
