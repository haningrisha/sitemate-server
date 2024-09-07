from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class Issue(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
