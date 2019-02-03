from django.db import models

class product(models.Model):
	pno=models.CharField(max_length=5, unique=True)
	pname=models.CharField(max_length=30)
	pcost=models.IntegerField()
	pmanufacturer=models.CharField(max_length=50)
	#pimg=models.ImageField()
	
class client(models.Model):
	cno=models.CharField(max_length=5,unique=True)
	cname=models.CharField(max_length=30)
	cadd=models.CharField(max_length=100)
	cpin=models.IntegerField()
	cstate=models.CharField(max_length=50)
	cbal=models.IntegerField()
	#pro= models.ForeignKey(product, on_delete=models.CASCADE,)
class order(models.Model):
	ono=models.CharField(max_length=5, unique=True)
	odate=models.DateField()
	ocid=models.ForeignKey(client, on_delete=models.CASCADE,)
	opid=models.ForeignKey(product, on_delete=models.CASCADE,)
	Oqty=models.IntegerField()
	ototal=models.IntegerField()
	opaystatus=models.BooleanField()

# Create your models here.
