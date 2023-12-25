from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
class UserManager(BaseUserManager):
    # def create_user(self, first_name,last_name,phone_number,email, password=None):
    #     # email=self.normalize_email(email),
    #     user = self.model(
    #         email=self.normalize_email(email),
    #         phone_number=phone_number,
    #         first_name=first_name,
    #         last_name=last_name,
    #     )
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    
    def create_superuser(self, first_name,last_name,phone_number, email,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
 
    last_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
   

    date_joined=models.DateTimeField(default=timezone.now)
    last_login=models.DateTimeField(default=timezone.now)
    created_date=models.DateTimeField(default=timezone.now)
    modified_date=models.DateTimeField(auto_now=True)   
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name','email']

    objects = UserManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class UserProfile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    amt=models.IntegerField(null=True,blank=True)
    interest=models.IntegerField(null=True,blank=True)


    def __str__(self):
        return self.user.first_name
     