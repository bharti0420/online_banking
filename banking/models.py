from django.db import models


# Create your models here.
GENDER_CHOICE=(
	("Male","Male"),
	("Female","Female"),
	)

class customer(models.Model):
	account_no=models.PositiveIntegerField(
		unique=True
		)
	username=models.CharField(unique=True,max_length=10)
	password=models.CharField(max_length=20)
	full_name=models.CharField(max_length=50,blank=False)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
	birth_date = models.DateField(null=True, blank=True)
	email = models.EmailField(unique=True, blank=False)
	contact_no = models.IntegerField(unique=True)
	balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
        )
	


class  deposite(models.Model):
	account_no=models.PositiveIntegerField()
	time_date = models.DateTimeField(auto_now_add=True)
	amount=models.DecimalField(default=0,
        max_digits=12,
        decimal_places=2
        )
	#def __str__(self,account_no):
	#	return self.account_no

class withdraw(models.Model):
	account_no=models.PositiveIntegerField()
	time_date = models.DateTimeField(auto_now_add=True)
	amount=models.DecimalField(default=0,
        max_digits=12,
        decimal_places=2
        )
	#def __init__(self):
	#	return self.account_no


