from django import forms
from .models import clerk,patient_register
class clerkform(forms.ModelForm):
    class Meta:
        model:clerk
        fields=['first_name','last_name','hospital_id']
class userform(forms.ModelForm):
    class Meta:
        model:patient_register
        fields=['first_name','last_name','cibil']