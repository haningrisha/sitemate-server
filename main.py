from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from routes import issue

app = FastAPI()
app.include_router(issue.router)

issues_db = {}


class Issue(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)