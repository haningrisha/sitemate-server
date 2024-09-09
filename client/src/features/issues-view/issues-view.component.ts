import { Component, OnInit } from '@angular/core';
import { IssuesService } from '../../services/issues.service';
import { CommonModule } from '@angular/common';
import {MatTableModule} from '@angular/material/table';
import { MatButtonModule } from '@angular/material/button';
import {
  MatDialog,
} from '@angular/material/dialog';
import { IssueFormComponent } from './issue-form/issue-form.component';
import { Subject, switchMap, tap } from 'rxjs';
import { Issue } from '../../models/issue.model';

@Component({
  selector: 'app-issues-view',
  standalone: true,
  imports: [CommonModule, MatTableModule, MatButtonModule],
  templateUrl: './issues-view.component.html',
  styleUrl: './issues-view.component.scss'
})
export class IssuesViewComponent implements OnInit {
  constructor(private issueService: IssuesService, private dialog: MatDialog) {}

  issues$ = new Subject<Issue[]>()
  columns = ['id', 'title', 'description', 'action']

  ngOnInit(): void {
      this.loadData().subscribe()
  }

  openDialog() {
    const ref = this.dialog.open(IssueFormComponent)
    ref.afterClosed().pipe(
      switchMap(() => {
        return this.loadData()
      })
    ).subscribe()
  }

  deleteIssue(id: string) {
    this.issueService.deleteIssue(id).pipe(
      switchMap(() => this.loadData())
    ).subscribe()
  }

  loadData() {
    return this.issueService.getIssues().pipe(
      tap((issues: Issue[]) => {
        this.issues$.next(issues)
      })
    )
  }
}
