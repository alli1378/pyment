from django.db import models
from django.utils import timezone
from user.models import User
# Create your models here.
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
class CheckingAccount(models.Model):
    '''
    '''
    balance =models.IntegerField()
    user =models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name='checking_user',
        null=True

    )
    

class SavingAccount(models.Model):
    '''
    '''
    balance =models.IntegerField()
    created =models.DateTimeField(default=timezone.now)
    exp =models.DateTimeField(default=timezone.now,verbose_name='')
    checking =models.ForeignKey(
        CheckingAccount,
        on_delete=models.SET_NULL,
        related_name='saving_checking',
        null=True )
   

class Transaction(models.Model):
    '''
    '''
    balance =IntegerRangeField(min_value=10000, max_value=3000000)
    created =models.DateTimeField(default=timezone.now)
    from_account=models.ForeignKey(
        CheckingAccount,
        on_delete=models.SET_NULL,
        related_name='from_user',
        null=True
    )
    to_account=models.ForeignKey(
        CheckingAccount,
        on_delete=models.SET_NULL,
        related_name='to_user',
        null=True

    )
