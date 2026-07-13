from pydantic import BaseModel, ConfigDict, Field, field_validator


class User(BaseModel):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1, max_length=200)

    @field_validator("name")
    @classmethod
    def name_must_be_not_empty(cls, v: str) -> str:
        res = v.strip()
        if not res:
            raise ValueError("Имя не может быть пустым")
        return res
