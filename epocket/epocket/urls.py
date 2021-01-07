"""epocket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from epocketapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    #  path('contact',views.contact,name='contact'),
     path('reg',views.reg,name='reg'),
     path('userhome',views.userhome,name='userhome'),
     path('expense',views.expense,name='expense'),
     path('income',views.income,name='income'),
     path('incometype',views.incometype,name='incometype'),
     path('expensetype',views.expensetype,name='expensetype'),
     path('budget',views.budget,name='budget'),
     path('budgetlist',views.budgetlist,name='budgetlist'),
     path('allbudget',views.allbudget,name='allbudget'),
     path('budgetview',views.budgetview,name='budgetview'),
     path('dates',views.dates,name='dates'),
     path('graph',views.graph,name='graph'),
     path('idate',views.idate,name='idate'),
     path('jsonIncome',views.jsonIncome,name='jsonIncome'),
     path('edate',views.edate,name='edate'),
     path('jsonExpense',views.jsonExpense,name='jsonExpense'),
     path('loan',views.loan,name='loan'),
     path('savings',views.savings,name='savings'),
]

