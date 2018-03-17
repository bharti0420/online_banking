from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
# Create your views here.

def online_home(request):
	return render(request,'banking/online_home.html',{})
def home(request):
	if(request.method=='POST'):
		form=customerForm(request.POST)
		if form.is_valid():
			account_no=form.cleaned_data['account_no']
			ins=customer(account_no=account_no)
			ins.username=form.cleaned_data['username']
			ins.password=form.cleaned_data['password']
			ins.full_name=form.cleaned_data['full_name']
			ins.gender=form.cleaned_data['gender']
			ins.birth_date=form.cleaned_data['birth_date']
			ins.email=form.cleaned_data['email']
			ins.contact_no=form.cleaned_data['contact_no']
			ins.balance=form.cleaned_data['balance']
			ins.save()
			#var="Thank You"
			return render(request,'base.html',{})

	else:	
		
		form=customerForm()
	return render(request,'banking/home.html',{'form':form})

def about(request):
	return render(request,'banking/about.html',{})

def deposite1(request):
	if(request.method=='POST'):
		form=depositeForm(request.POST)
		if form.is_valid():
			account=form.cleaned_data['account_no']
			amount=form.cleaned_data['amount']
			try:
				ins=customer.objects.get(account_no=account)
				#print("hello")
				#print(ins)
				x=int(ins.balance)
				print(x)
				x=x+amount
				ins.balance=x
				ins.save()
				#account_no=form.cleaned_data['account_no']
				ins=deposite()
				ins.amount=amount
				#ins.time_date=form.cleaned_data['time_date']
				ins.account_no=account
				ins.save()
				var="Deposit Done"
				return render(request,'banking/general.html',{'var':var})
			except:

				return render(request,'banking/except.html',{})
	else:
		form=depositeForm()
	return render(request,'banking/deposite.html',{'form':form})

def withdrawal(request):
	if(request.method=='POST'):
		form=withdrawForm(request.POST)
		if form.is_valid():
			account=form.cleaned_data['account_no']
			try:
				ins=customer.objects.get(account_no=account)
				amount=form.cleaned_data['amount']
				x=int(ins.balance)
				if(amount>0 and amount<x):
					x=x-amount
					ins.save()
					ins=withdraw()
					ins.amount=amount
					ins.account_no=account
					ins.save()
					var="Withdrawal Done"
					return render(request,'banking/general.html',{'var':var})
				else:
					var="Invalid Amount"
					return render(request,'banking/general.html',{'var':var})

			except:
				return render(request,'banking/except.html',{})


	else:
		form=withdrawForm()
	return render(request,'banking/withdraw.html',{'form':form})

def account_info(request):
	if(request.method=='POST'):
		form=account_infoForm(request.POST)
		if form.is_valid():
			account=form.cleaned_data['account_no']
			try:
				ins=customer.objects.get(account_no=account)
				Account=account
				Name=ins.full_name
				Balance=ins.balance
				Email=ins.email
				context={'Account':Account,'Name':Name,'Balance':Balance,'Email':Email}
				return render(request,'banking/bal_info.html',context)


			except:
				return render(request,'banking/except.html',{})

	else:
		form=account_infoForm()
	return render(request,'banking/account_info.html',{'form':form})


def payment(request):
	if(request.method=='POST'):
		form=paymentForm(request.POST)
		if form.is_valid():
			account_from=form.cleaned_data['from_account']
			account_to=form.cleaned_data['to_account']
			try:
				insf=customer.objects.get(account_no=account_from)
				inst=customer.objects.get(account_no=account_to)
				amount=form.cleaned_data['amount']
				date=form.cleaned_data['date']
				x_f=int(insf.balance)
				x_t=int(inst.balance)
				if(amount>0 and amount<=x_f):
					x_f=x_f-amount
					insf.balance=x_f
					x_t+=amount
					inst.balance=x_t
					inst.save()
					insf.save()
					insf=withdraw(account_no=account_from)	#object of withdraw table
					insf.time_date=date
					insf.amount=amount
					insf.account_no=account_from
					insf.save()
					insf=deposite(account_no=account_to)	#object of deposite table
					insf.time_date=date
					insf.amount=amount
					insf.account_no=account_to
					insf.save()
					var="transfer done"

					return render(request,'banking/general.html',{'var':var})
				else:
					var="Not enough amount in account"
					return render(request,'banking/general.html',{'var':var})

			except:
				return render(request,'banking/except.html',{})
	else:
		form=paymentForm()
	return render(request,'banking/payment.html',{'form':form})

	
def transaction(request):
	if(request.method=='POST'):
		form=transactionForm(request.POST)
		if form.is_valid():
			account=form.cleaned_data['account_no']
			try:
				ins=customer.objects.get(account_no=account)
				ins.account_no=account

				try:
					query='SELECT * FROM banking_withdraw WHERE account_no=%s' %account
					value=withdraw.objects.raw(query)
					countw=len(list(value))
				except:
					value="No withdraw transaction"
				try:
					query='SELECT * FROM banking_deposite WHERE account_no=%s' %account
					value1=deposite.objects.raw(query)
					countd=len(list(value1))
					print (countd)
				except:
					value1="No deposite transaction"
				if(countw>0 and countd>0):
					return render(request,'banking/transaction.html',{'value':value,'value1':value1,'account':account})
				elif(countw>0 and countd<1):
					value1="No deposite transaction"
					return render(request,'banking/transactionw.html',{'value':value,'value1':value1,'account':account})
				elif(countw<1 and countd>0):
					value="No withdraw transaction"
					return render(request,'banking/transactiond.html',{'value':value,'value1':value1,'account':account})
				else:
					var="No Transaction Done"
					return render(request,'banking/general.html',{'var':var})
						
			except:
				return render(request,'banking/except.html',{})
	else:
		form=transactionForm()
	return render(request,'banking/account_info.html',{'form':form})

def login(request):
	if(request.method=='POST'):
		form=loginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			try:
				ins=customer.objects.get(username=username)
				password=form.cleaned_data['password']
				if(password==ins.password):
					return render(request,'base.html',{})
				else:
					print ("hello else")
					return HttpResponse("wrong password")
			except:
				return HttpResponse("username name doesn't exist")
	else:
		form=loginForm()
	return	render(request,'banking/login.html',{'form':form})


