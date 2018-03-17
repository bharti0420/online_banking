from django.urls import path
from . import views

urlpatterns=[
	path('',views.online_home,name='online_home'),
	path('login/',views.login,name='login'),
	path('signUp/',views.home,name='home'),
	path('about/',views.about,name='about'),
	path('deposite/',views.deposite1,name='deposite'),
	path('withdraw/',views.withdrawal,name='withdraw'),
	path('account_info/',views.account_info,name='account_info'),
	path('transfer/',views.payment,name='payment'),
	path('transaction_detail/',views.transaction,name='transaction'),
]
