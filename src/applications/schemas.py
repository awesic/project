import datetime

from pydantic import BaseModel

from src.applications.models import Corpus, Status


class ApplicationBase(BaseModel):
    id: int
    corpus: Corpus
    auditorium: str
    incident_category: str
    problem: str
    status: Status

    class Config:
        orm_mode = True


class CreatApplication(BaseModel):
    corpus: Corpus
    auditorium: str
    incident_category: str
    problem: str

    class Config:
        orm_mode = True


class ReadApplication(BaseModel):
    id: int
    created_at: datetime.datetime
    status: Status

    class Config:
        orm_mode = True