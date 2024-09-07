from fastapi import APIRouter
from fastapi import HTTPException
from typing import List
from uuid import uuid4, UUID


router = APIRouter(
    prefix='/account',
    tags=['account'],
    responses={404: {'description': 'Not found'}},
)


@router.post("/issues/", response_model=Issue)
def create_issue(issue: Issue):
    issue.id = uuid4()
    issues_db[issue.id] = issue
    return issue


@router.get("/issues/", response_model=List[Issue])
def read_issues():
    return list(issues_db.values())


@router.get("/issues/{issue_id}", response_model=Issue)
def read_issue(issue_id: UUID):
    if issue_id not in issues_db:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issues_db[issue_id]


@router.put("/issues/{issue_id}", response_model=Issue)
def update_issue(issue_id: UUID, updated_issue: Issue):
    if issue_id not in issues_db:
        raise HTTPException(status_code=404, detail="Issue not found")

    updated_issue.id = issue_id
    issues_db[issue_id] = updated_issue
    return updated_issue


@router.delete("/issues/{issue_id}")
def delete_issue(issue_id: UUID):
    if issue_id not in issues_db:
        raise HTTPException(status_code=404, detail="Issue not found")

    del issues_db[issue_id]
    return {"detail": "Issue deleted successfully"}
