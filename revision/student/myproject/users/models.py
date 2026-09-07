from django.db import models
from datetime import datetime, timezone 
import uuid 

 
from django.conf import settings 
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin

from django.utils.translation import gettext as _ 
from django.core.validators import MaxLengthValidator,MinLengthValidator 
 
 
class UserManager(BaseUserManager): 
    def create_user(self, phone_number, first_name, last_name, username, email, 
password=None, **extra_fields): 
        user = self.model(            
            phone_number=phone_number, 
            first_name=first_name, 
            last_name=last_name, 
            username=username, 
            email=email, 
            **extra_fields, 
        ) 
        user.set_password(password) 
        user.save(using=self._db) 
        return user 
     
    def create_superuser(self,first_name, last_name, username, email,phone_number=None, 
     password=None, **extra_fields): 
        user = self.create_user( 
            phone_number=phone_number, 
            first_name=first_name, 
            last_name=last_name, 
            username=username, 
            email=email, 
            password=password, 
            user_type=User.ADMIN, 
            **extra_fields 
        ) 
        user.is_staff = True 
        user.save(using=self._db) 
        return user 
 
 
 
 
class User(AbstractBaseUser, PermissionsMixin): 
 
    ADMIN="SUPER ADMIN" 
    STAFF="STAFF" 
    STUDENT_ADMIN="Student Admin" 
    STUDENT_NAME = "Student Name"
    STUDENT_DEPARTMENT="Student Department" 
    STUDENT_EMAIL="Student Email" 
   
     
     
    USER_TYPE_CHOICE = ( 
        (ADMIN,"Super Admin"), 
        (STAFF,"Staff"), 
        (STUDENT_ADMIN,"Student Admin"), 
        (STUDENT_NAME,"Student Name"), 
        (STUDENT_DEPARTMENT,"Student Department"), 
        (STUDENT_EMAIL,"Student Email"),
        
    ) 
     
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False) 
    username = models.CharField(_("username"), max_length=100,unique=True) 
    first_name=models.CharField(_("first name"), max_length=100) 
    last_name=models.CharField(_("last name"), max_length=100) 
    phone_number = models.CharField( 
        _("phone number"), max_length=255,validators=[ 
            MinLengthValidator(limit_value=10), 
            MaxLengthValidator(limit_value=10) 
        ], blank=True, null=True,unique=True 
    ) 
    email = models.EmailField(_('email address'), blank=True, null=True,unique=True) 
    user_type = models.CharField( 
        _("user type"), choices=USER_TYPE_CHOICE, 
max_length=50,default=STUDENT_NAME) 
     
    is_active = models.BooleanField(_("is active"), default=True) 
    is_staff = models.BooleanField(_("is staff"), default=False) 
     
    created_at = models.DateTimeField(_("created at"), auto_now_add=True) 
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)  
    objects = UserManager() 
    is_staff = models.BooleanField(_("is staff"), default=False) 
     
    USERNAME_FIELD = _("username") 
    LOGIN_FIELDS = ["username","email","phone_number"] 
    REQUIRED_FIELDS = ["first_name","last_name","email"] 
 
    def get_full_name(self): 
        # The user is identified by their address 
        return f"{self.first_name} {self.last_name}" 
 
 
    def __str__(self):  # __unicode__ on Python 2O 
        return f"{self.first_name} {self.last_name}" 
 
    def has_perm(self, perm, obj=None): 
        "Does the user have a specific permission?" 
        # Simplest possible answer: Yes, always 
        return True 
 
    def has_module_perms(self, app_label): 
        "Does the user have permissions to view the app `app_label`?" 
        # Simplest possible answer: Yes, always 
        return True 
 
    @property 
    def facility(self): 
        try: 
            return self.facility_staff_roles.last().facility 
        except: 
            return None 
     
    @property 
    def role(self): 
        return self.user_type