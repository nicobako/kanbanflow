import pydantic
import humps


def _gen_alias(key: str):
    if "id" == key:
        return "_id"
    else:
        return humps.camelize(key)


class BaseModel(pydantic.BaseModel):
    class Config:
        alias_generator = _gen_alias
        extra = "forbid"
        allow_mutation = False
