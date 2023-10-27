from import_export import resources
from Caledon_Reno_Work_Hours.models import Job


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Job
