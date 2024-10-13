from rest_framework import serializers
from account.models import SavingAccount,CheckingAccount,Transaction
from django.db import IntegrityError, transaction
class SavingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingAccount
        fields = ('balance', 'exp')
    def _user(self):
        request = self.context.get('request', None)
        if request:
            user=request.user
            return user
    def validate(self, attrs):
        data_checking=CheckingAccount.objects.get(user=self._user())
        if data_checking is not None and data_checking.balance<attrs['balance']:
            raise serializers.ValidationError(
                {"balance": "Checking Balance is more than your Saving Balance."})
        return attrs
    @transaction.atomic
    def create(self,validated_data):
        data_checking=CheckingAccount.objects.get(user=self._user())
        CheckingAccount.objects.filter(user=self._user()).update(balance=data_checking.balance-validated_data['balance'])
        data = SavingAccount.objects.create(balance=validated_data['balance'],checking=data_checking)
        Transaction.objects.create(balance=validated_data['balance'],from_account=data_checking)
        return data
class CheckingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckingAccount
        fields = ('balance','user')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
    def _user(self):
        request = self.context.get('request', None)
        if request:
            user=request.user
            return user
class TransactionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['balance','to_account']
    def _user(self):
        request = self.context.get('request', None)
        if request:
            user=request.user
            return user
    def validate(self, attrs):
        data_checking=CheckingAccount.objects.get(user=self._user())
        if data_checking.id==attrs['to_account'].id:
            raise serializers.ValidationError(
                {"balance": "Checking Balance is more than your Saving Balance."})
        if data_checking is not None and data_checking.balance<attrs['balance'] :
            raise serializers.ValidationError(
                {"balance": "Checking Balance is more than your Saving Balance."})
        return attrs
    @transaction.atomic
    def create(self,validated_data):
        print(validated_data['to_account'].id)
        data_checking=CheckingAccount.objects.get(user=self._user())
        data_checking2=CheckingAccount.objects.get(pk=validated_data['to_account'].id)
        CheckingAccount.objects.filter(user=self._user()).update(balance=data_checking.balance-validated_data['balance'])
        CheckingAccount.objects.filter(pk=validated_data['to_account'].id).update(balance=data_checking2.balance+validated_data['balance'])
        data=Transaction.objects.create(balance=validated_data['balance'],from_account=data_checking,to_account=validated_data['to_account'])
        return data
    