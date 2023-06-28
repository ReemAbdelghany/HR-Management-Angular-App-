from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from HRApp.serializers import BranchSerializer, EmployeeSerializer
from HRApp.models import Branch, Employee
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def branchApi(request, id=0):
    if request.method == 'GET':
        branches = Branch.objects.all()
        branch_serializer = BranchSerializer(branches, many=True)
        return JsonResponse(branch_serializer.data, safe=False)
    elif request.method == 'POST':
        branch_data = JSONParser().parse(request)
        branch_serializer = BranchSerializer(data=branch_data)
        if branch_serializer.is_valid():
            branch_serializer.save()
            return JsonResponse("Branch added successfully", safe=False)
        return JsonResponse(branch_serializer.errors, status=400)
    elif request.method == 'PUT':
        branch_data = JSONParser().parse(request)
        try:
            branch = Branch.objects.get(b_id=id)
        except Branch.DoesNotExist:
            return JsonResponse("Branch does not exist", status=404)
        branch_serializer = BranchSerializer(branch, data=branch_data)
        if branch_serializer.is_valid():
            branch_serializer.save()
            return JsonResponse("Branch updated successfully", safe=False)
        return JsonResponse(branch_serializer.errors, status=400)
    elif request.method == 'DELETE':
        try:
            branch = Branch.objects.get(b_id=id)
            branch.delete()
            return JsonResponse("Branch deleted successfully", safe=False)
        except Branch.DoesNotExist:
            return JsonResponse("Branch does not exist", status=404)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Employee added successfully", safe=False)
        return JsonResponse(employee_serializer.errors, status=400)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        try:
            employee = Employee.objects.get(e_id=id)
        except Employee.DoesNotExist:
            return JsonResponse("Employee does not exist", status=404)
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Employee updated successfully", safe=False)
        return JsonResponse(employee_serializer.errors, status=400)
    elif request.method == 'DELETE':
        try:
            employee = Employee.objects.get(e_id=id)
            employee.delete()
            return JsonResponse("Employee deleted successfully", safe=False)
        except Employee.DoesNotExist:
            return JsonResponse("Employee does not exist", status=404)
