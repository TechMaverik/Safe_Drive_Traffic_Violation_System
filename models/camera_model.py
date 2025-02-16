from pydantic import BaseModel


class CameraPath(BaseModel):
    camera1_path: str
    camera2_path: str
    camera3_path: str
    camera4_path: str
