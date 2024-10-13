from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
# from account.models import CheckingAccount,SavingAccount
# Create your models here.
class User(AbstractUser):
    '''
    '''
    objects=UserManager()
