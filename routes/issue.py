from fastapi import APIRouter
from typing import List
from uuid import UUID
from fastapi import HTTPException
from models.issue import Issue
from crud import issue_crud


router = APIRouter(
    prefix='/account',
    tags=['account'],
    responses={404: {'description': 'Not found'}},
)


@router.post("/issues/", response_model=Issue)
def create_issue(issue: Issue):
    return issue_crud.create_issue(issue)


@router.get("/issues/", response_model=List[Issue])
def read_issues():
    return issue_crud.read_issues()


@router.get("/issues/{issue_id}", response_model=Issue)
def read_issue(issue_id: UUID):
    issue = issue_crud.read_issue(issue_id)
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue


@router.put("/issues/{issue_id}", response_model=Issue)
def update_issue(issue_id: UUID, updated_issue: Issue):
    updated_issue.id = issue_crud.update_issue(issue_id, updated_issue)
    if updated_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return updated_issue


@router.delete("/issues/{issue_id}")
def delete_issue(issue_id: UUID):
    deleted_issue = issue_crud.delete_issue(issue_id)
    if deleted_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return deleted_issue
