from uuid import uuid4, UUID
from typing import List
from models.issue import Issue
from loguru import logger

issues_db = {}


def create_issue(issue: Issue) -> Issue:
    issue.id = uuid4()
    issues_db[issue.id] = issue
    logger.info(f'Issue {issue.id} created', issue)
    return issue


def read_issues() -> List[Issue]:
    return list(issues_db.values())


def read_issue(issue_id: UUID) -> Issue | None:
    return issues_db.get(issue_id)


def update_issue(issue_id: UUID, updated_issue: Issue) -> Issue | None:
    if issue_id not in issues_db:
        return None

    updated_issue.id = issue_id
    issues_db[issue_id] = updated_issue
    logger.info(f'Issue {issue_id} updated', updated_issue)
    return updated_issue


def delete_issue(issue_id: UUID) -> Issue | None:
    if issue_id not in issues_db:
        return None

    deleted_issue = issues_db.pop(issue_id)
    logger.info(f'Issue {issue_id} deleted', deleted_issue)
    return deleted_issue
