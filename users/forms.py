from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, SelectDateWidget
from Caledon_Reno_Work_Hours.models import FilledForm, Job, Application, Estimate
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from import_export import resources


JOB_CHOICES= [
    ('Delivery', 'Delivery'),
    ('Demolition', 'Demolition'),
    ('Plumbing', 'Plumbing'),
    ('HVAC', 'HVAC'),
    ('Electrical', 'Electrical'),
    ('Drywall', 'Drywall'),
    ('Painting', 'Painting'),
    ('Flooring', 'Flooring'),
    ('Waterproofing', 'Waterproofing'),
    ('Tiling', 'Tiling'),
    ('Trim', 'Trim'),
    ('Inspection', 'Inspection'),
    ('Estimating', 'Estimating'),
    ('Design', 'Design'),
    ('Cleaning', 'Cleaning'),
    ('Cabinetry', 'Cabinetry'),
    ]


class EstimateRequest(ModelForm):
    First_name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    Last_name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    Email = forms.EmailInput()
    Company = forms.CharField()
    Phone = forms.NumberInput()
    City = forms.TextInput()
    Zip_code = forms.CharField()
    Address = forms.CharField()
    Blueprints_and_Images = forms.FileInput()

    class Meta:
        model = Estimate
        fields = ['First_name', 'Last_name', 'Email', 'Company', 'Phone', 'City', 'Zip_code', 'Address',
                  'Blueprints_and_Images']


class ApplicationForm(ModelForm):
    First_name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    Last_name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    Email = forms.EmailInput()
    Resume = forms.FileInput()

    class Meta:
        model = Application
        fields = ['First_name', 'Last_name', 'Email', 'Resume']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UploadForm(ModelForm):

    First_name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    Last_name = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    Email = forms.EmailInput()
    Mileage = forms.FloatField(initial=0)
    Expense_Image = forms.ClearableFileInput()
    Expense_Amount = forms.FloatField(initial=0)
    Client = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    Date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
    Work_type = forms.CharField(widget=forms.Select(choices=JOB_CHOICES))
    Time_started = forms.TimeField(
        widget=TimePicker(
            options={

                'defaultDate': '1970-01-01T12:00:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ),
    )
    Time_ended = forms.TimeField(
        widget=TimePicker(
            options={
                'defaultDate': '1970-01-01T12:00:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ),
    )
    Rating = forms.IntegerField()
    Notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)
    What_did_you_learn = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)

    class Meta:
        model = FilledForm
        fields = ['First_name', 'Last_name', 'Email', 'Mileage', 'Expense_Image', 'Expense_Amount',
                  'Client', 'Date', 'Work_type', 'Time_started', 'Time_ended', 'Rating', 'Notes', 'What_did_you_learn']


class UploadDB(forms.Form):
    class Meta:
        model = Job
        fields = '__all__'
        skip_unchanged = True
        use_bulk = True
