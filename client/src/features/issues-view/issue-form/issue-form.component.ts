import { Component } from '@angular/core';
import { FormGroup, FormBuilder, Validators, ReactiveFormsModule } from '@angular/forms';
import { Issue } from '../../../models/issue.model';
import { IssuesService } from '../../../services/issues.service';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatSelectModule } from '@angular/material/select';
import { MatIconModule } from '@angular/material/icon';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-issue-form',
  standalone: true,
  imports: [
    MatInputModule,
    MatFormFieldModule,
    MatButtonModule,
    MatSelectModule,
    MatIconModule,
    ReactiveFormsModule
  ],
  templateUrl: './issue-form.component.html',
  styleUrl: './issue-form.component.scss',
})
export class IssueFormComponent {
  issueForm: FormGroup;

  constructor(private fb: FormBuilder, private issueService: IssuesService, private dialogRef: MatDialogRef<IssueFormComponent>) {
    this.issueForm = this.fb.group({
      title: ['', Validators.required],
      description: [''],
    });
  }

  onSubmit(): void {
    if (this.issueForm.valid) {
      const newIssue: Issue = this.issueForm.value;
      this.issueService.createIssue(newIssue).subscribe(
        (response) => {
          console.log('Issue created successfully:', response);
          this.issueForm.reset();
          this.dialogRef.close()
        },
        (error) => {
          console.error('Error creating issue:', error);
        }
      );
    }
  }
}
