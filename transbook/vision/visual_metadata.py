from typing import Literal

from pydantic import BaseModel


class VisualMetadata(BaseModel):
    block_id: str
    background_color: str
    estimated_text_color: str | None = None
    background_variance: float
    background_mode: Literal["solid", "simple", "complex"]
    recommended_render_mode: Literal["replace", "callout", "manual_review"]