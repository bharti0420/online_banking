from django import forms
from django.forms import ModelForm
from .models import *
from datetime import datetime

class customerForm(ModelForm):
	class Meta:
		model=customer
		widgets = {'password': forms.PasswordInput()}
		fields = "__all__"
		
class depositeForm(ModelForm):
	class Meta:
		model=deposite
		fields="__all__"

class withdrawForm(ModelForm):
	class Meta:
		model=withdraw
		fields="__all__"

class account_infoForm(forms.Form):
	account_no=forms.IntegerField()

class paymentForm(forms.Form):
	from_account=forms.IntegerField()
	to_account=forms.IntegerField()
	amount=forms.IntegerField()
	date=forms.DateTimeField(initial=datetime.now())

class transactionForm(forms.Form):
	account_no=forms.IntegerField()

class loginForm(forms.Form):
	username=forms.CharField(max_length=10)
	password=forms.CharField(max_length=20,widget=forms.PasswordInput())
	#widgets = {'password': forms.PasswordInput()}
	
	"""class Meta:
		model=customer
		widgets = {'password': forms.PasswordInput()}
		fields = ('username', 'password')"""
	
