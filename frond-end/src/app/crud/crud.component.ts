import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-crud',
  templateUrl: './crud.component.html',
  styleUrls: ['./crud.component.scss']
})
export class CrudComponent implements OnInit {
  branches: any[] = [];
  employees: any[] = [];
  branchFormValues: any = {};
  employeeFormValues: any = {};
  branchFormTitle: string = 'Create Branch';
  employeeFormTitle: string = 'Create Employee';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.getBranches();
    this.getEmployees();
  }

  getBranches() {
    this.http.get<any>('http://localhost:8000/branches/').subscribe(data => {
      this.branches = data;
    });
  }

  getEmployees() {
    this.http.get<any>('http://localhost:8000/employees/').subscribe(data => {
      this.employees = data;
    });
  }

  submitBranchForm() {
    if (this.branchFormValues.b_id) {
      this.updateBranch();
    } else {
      this.createBranch();
    }
  }

  createBranch() {
    this.http.post<any>('http://localhost:8000/branches/', this.branchFormValues).subscribe(data => {
      this.getBranches();
      this.resetBranchForm();
    });
  }

  updateBranch() {
    this.http.put<any>(`http://localhost:8000/branches/${this.branchFormValues.b_id}/`, this.branchFormValues).subscribe(data => {
      this.getBranches();
      this.resetBranchForm();
    });
  }

  editBranch(branch: any) {
    this.branchFormValues = { ...branch };
    this.branchFormTitle = 'Edit Branch';
  }

  deleteBranch(branch: any) {
    this.http.delete<any>(`http://localhost:8000/branches/${branch.b_id}/`).subscribe(data => {
      this.getBranches();
    });
  }

  submitEmployeeForm() {
    if (this.employeeFormValues.e_id) {
      this.updateEmployee();
    } else {
      this.createEmployee();
    }
  }

  createEmployee() {
    this.http.post<any>('http://localhost:8000/employees/', this.employeeFormValues).subscribe(data => {
      this.getEmployees();
      this.resetEmployeeForm();
    });
  }

  updateEmployee() {
    this.http.put<any>(`http://localhost:8000/employees/${this.employeeFormValues.e_id}/`, this.employeeFormValues).subscribe(data => {
      this.getEmployees();
      this.resetEmployeeForm();
    });
  }

  editEmployee(employee: any) {
    this.employeeFormValues = { ...employee };
    this.employeeFormTitle = 'Edit Employee';
  }

  deleteEmployee(employee: any) {
    this.http.delete<any>(`http://localhost:8000/employees/${employee.e_id}/`).subscribe(data => {
      this.getEmployees();
    });
  }

  resetBranchForm() {
    this.branchFormValues = {};
    this.branchFormTitle = 'Create Branch';
  }

  resetEmployeeForm() {
    this.employeeFormValues = {};
    this.employeeFormTitle = 'Create Employee';
  }

  getBranchName(branchId: number) {
    const branch = this.branches.find(branch => branch.b_id === branchId);
    return branch ? branch.b_name : 'No Branch';
  }

  getEmployeeName(employeeId: number) {
    const employee = this.employees.find(employee => employee.e_id === employeeId);
    return employee ? employee.e_name : 'No Manager';
  }
}
