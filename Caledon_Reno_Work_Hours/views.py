from django.shortcuts import render
from django.views.generic import CreateView
from .models import FilledForm, Job
from django.http import HttpResponse
from Caledon_Reno_Work_Hours.templates import Caledon_Reno_Work_Hours
from users.forms import UploadForm, ApplicationForm, EstimateRequest
from rest_framework import generics, parsers
import pandas as pd
from tablib import Dataset
from django.shortcuts import render
from openpyxl import load_workbook
from .models import Job
from django_project.resources import EmployeeResource


def import_from_excel(request):
    if request.method == 'POST' and 'my_file' in request.FILES:
        employee_resource = EmployeeResource()
        dataset = Dataset()
        new_Job = request.FILES["my_file"]
        imported_data = dataset.load(new_Job.read(), format='xlsx')
        for data in imported_data:
            value = Job(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],

            )

    return render(request, 'Caledon_Reno_Work_Hours/form.html')

    # return render(request, 'Caledon_Reno_Work_Hours/import_excel_db.html')


# def postDB(request, *args, **kwargs):
#     file = request.FILES.get(r"C:\Users\cany8\Downloads\Anthony_Exmples.xlsx")
#     df = pd.read_excel(file)
#     rename_columns = {'Key': 'Key', 'Phase': 'Phase', 'Description': 'Description',
#                       'Specific_Description': 'Specific_Description', "Unit_Cost": 'Unit_cost',
#                       'Unit_Type': 'Unit_type', 'GC_Rate_10': 'GC_Rate_10',
#                       'Retail_Rate_40': 'Retail_Rate_40'}
#     df.rename(columns=rename_columns, inplace=True)
#     job = Job()
#     dataset = Dataset().load(df)
#     result = job.import_data(dataset, dry_run=True, raise_errors=True)
#     if not result.has_errors():
#         result = job.import_data(dataset, dry_run=False)
#         return HttpResponse()


class ImportDB(generics.GenericAPIView):
    parser_classes = [parsers.MultiPartParser]


def home(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'Caledon_Reno_Work_Hours/home.html', {'form': UploadForm})


def homepage(request):
    return render(request, 'Caledon_Reno_Work_Hours/homepage.html')


def apply(request):
    if request.POST:
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'Caledon_Reno_Work_Hours/apply.html', {'form': ApplicationForm})


def estimate(request):
    if request.POST:
        form = EstimateRequest(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'Caledon_Reno_Work_Hours/estimate.html', {'form': EstimateRequest})


