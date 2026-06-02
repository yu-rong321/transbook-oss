from typing import Literal

from pydantic import BaseModel, Field, field_validator


class BBox(BaseModel):
    x: float
    y: float
    width: float
    height: float

    @field_validator("width", "height")
    @classmethod
    def must_be_positive(cls, value: float) -> float:
        if value <= 0:
            raise ValueError("bbox width and height must be positive")
        return value


class OCRBlock(BaseModel):
    id: str
    text: str
    bbox: BBox
    score: float = Field(ge=0.0, le=1.0)
    source: Literal["mock", "paddleocr", "vision"] = "mock"


class OCRPageResult(BaseModel):
    image_width: int
    image_height: int
    blocks: list[OCRBlock]