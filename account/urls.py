"""
URL configuration for payment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account.views import TransactionList,CheckingAccountCreate,SavingAccountCreate,CheckingAccountUpdate,TransactionCreate
urlpatterns = [
    # jwt
    # 
    path('transaction/create/',TransactionCreate.as_view(), name='transaction-creat'),
    path('transaction/list/',TransactionList.as_view(), name='transaction-list'),
    path('checking/create/',CheckingAccountCreate.as_view(), name='checking-create'),
    path('checking/update/',CheckingAccountUpdate.as_view(), name='checking-update'),
    path('saving/create/',SavingAccountCreate.as_view(), name='saveing-create'),
]
