import pydantic
import humps

class BaseModel(pydantic.BaseModel):
    class Config:
        extra="forbid"
        allow_mutation=False
