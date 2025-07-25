from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError("Email is required")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            is_staff = False ,
            is_active = True , 
            is_admin = False , 
            is_superuser = False
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone, password):
        user = self.create_user(email, first_name, last_name, phone, password)
        user.is_admin = True
        user.is_staff = True  # Add is_staff for admin access
        user.is_superuser = True  # Optional: for full admin privileges
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Add is_staff
    is_admin = models.BooleanField(default=False)  # Keep is_admin if needed
    is_superuser = models.BooleanField(default=False)  # Optional: for superuser

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email

    # Optional: Define permissions methods if using is_superuser
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
    


## Making the model to store the personal information
class ProfileDetails(models.Model):

    user = models. OneToOneField(User , on_delete= models.CASCADE)
    dob = models.DateField(null = True , blank = True)
    occupation = models.CharField(max_length= 200)
    skill  = models.CharField(max_length = 200)
    experience = models.IntegerField(default=0)
    location = models.CharField(max_length = 200)
    workLink = models.URLField()
    description  = models.CharField(max_length = 1000)
    achievements = models.CharField(max_length= 500)
    profile_picture = models.ImageField(upload_to = 'profile_pics/' , null = True , blank = True)

    def __str__(self):
        return f'{self.user.first_name} Profile'