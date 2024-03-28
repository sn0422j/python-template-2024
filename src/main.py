import datetime

from pydantic import BaseModel


class MainClass(BaseModel):
    time: datetime.datetime
