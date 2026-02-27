from pydantic import BaseModel, Field


class InterrogateRequest(BaseModel):
    image: str = Field(default="", title="Image", description="Image to interrogate")
    model: str = Field(
        default="wd14-convnextv2-v2", title="Model", description="Model to use"
    )
    threshold: float = Field(default=0.35, title="Threshold", description="Threshold")


class TaggerInterrogateRequest(InterrogateRequest):
    queue: str = Field(default="", title="Queue", description="Queue")
    name_in_queue: str = Field(
        default="", title="Name in queue", description="Name in queue"
    )


class InterrogateResponse(BaseModel):
    caption: dict = Field(default=None, title="Caption", description="Caption")


class TaggerInterrogateResponse(InterrogateResponse):
    pass


class TaggerInterrogatorsResponse(BaseModel):
    models: list[str] = Field(
        default_factory=list,
        title="Models",
        description="Available interrogator models",
    )
