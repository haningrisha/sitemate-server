from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID

app = FastAPI()

issues_db = {}


class Issue(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None


@app.post("/issues/", response_model=Issue)
def create_issue(issue: Issue):
    issue.id = uuid4()
    issues_db[issue.id] = issue
    return issue


@app.get("/issues/", response_model=List[Issue])
def read_issues():
    return list(issues_db.values())


@app.get("/issues/{issue_id}", response_model=Issue)
def read_issue(issue_id: UUID):
    if issue_id not in issues_db:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issues_db[issue_id]


@app.put("/issues/{issue_id}", response_model=Issue)
def update_issue(issue_id: UUID, updated_issue: Issue):
    if issue_id not in issues_db:
        raise HTTPException(status_code=404, detail="Issue not found")

    updated_issue.id = issue_id
    issues_db[issue_id] = updated_issue
    return updated_issue


@app.delete("/issues/{issue_id}")
def delete_issue(issue_id: UUID):
    if issue_id not in issues_db:
        raise HTTPException(status_code=404, detail="Issue not found")

    del issues_db[issue_id]
    return {"detail": "Issue deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)