from django.db import models
import re
from investor.models import User

#clerk ka signup
class clerk(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, default=None)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    hospital_id=models.CharField(max_length=100)
    is_approved=models.BooleanField(default=False)

    def __str__(self):
        return self.hospital_id
    



# class patient_login(models.Model):
# class patient_logout(models.Model):

class patient_register(models.Model):
    # user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, default=None)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    cibil=models.CharField(max_length=100)

    # def isValidPanCardNo(panCardNo):
    #     regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
    #     p = re.compile(regex)
 
    #     if(panCardNo == None):
    #         return False
    
    #     if(re.search(p, panCardNo) and len(panCardNo) == 10):
    #         return True
    #     else:
    #         return False

    #     is_approved=models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    
    # GENDER_CHOICES = [
    #     ('Male', 'Male'),
    #     ('Female', 'Female'),
    # ]

    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # father_name = models.CharField(max_length=100)
    # mother_name = models.CharField(max_length=100)
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # pan_number = models.CharField(max_length=10, unique=True)  
    # mobile_number = models.CharField(max_length=15)
    # occupation = models.CharField(max_length=100)
    # income = models.DecimalField(max_digits=10, decimal_places=2)
    # address = models.TextField()
    # pincode = models.CharField(max_length=10)

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
