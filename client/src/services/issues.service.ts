import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Issue } from '../models/issue.model';

const api = 'http://0.0.0.0:8000'

@Injectable({
  providedIn: 'root'
})
export class IssuesService {
  constructor(private httpClient: HttpClient) { }

  createIssue(issue: Issue) {
    return this.httpClient.post<Issue>(`${api}/issues/`, issue)
  }

  getIssue(id: string) {
    return this.httpClient.get<Issue>(`${api}/issues/${id}`)
  }

  getIssues() {
    return this.httpClient.get<Issue[]>(`${api}/issues/`)
  }
  
  updateIssue(id: string, issue: Issue) {
    return this.httpClient.put<Issue>(`${api}/issues/${id}`, issue)
  }

  deleteIssue(id: string) {
    return this.httpClient.delete<Issue>(`${api}/issues/${id}`)
  }
}
