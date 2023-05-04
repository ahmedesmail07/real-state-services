from django.db import models
from django import forms
class Payment(models.Model):
    codenumber = models.CharField(max_length=20)
    meterreding = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/images')
    comments = models.TextField()

    def __str__(self):
        return self.codenumber

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['codenumber', 'meterreding', 'company', 'comments', 'image']

class MeterRequest(models.Model):
    national_ID = models.IntegerField()
    name = models.CharField(max_length=50)
    meter_address = models.CharField(max_length=20)
    phone_num = models.IntegerField()
    address = models.CharField(max_length=30)
    block_num = models.IntegerField()
    phone_num2 = models.IntegerField()
    att_image = models.ImageField(upload_to='static/images')
    id_image = models.ImageField(upload_to='static/images')
    approvale_authority_name = models.CharField(max_length=50)
    approvale_authority = models.CharField(max_length=50)
    applicant = models.CharField(max_length=50)
    tax_num = models.IntegerField()
    Governorate =  models.CharField(max_length=10)
    Enterprise =  models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class MeterRequestForm(forms.ModelForm):
    class Meta:
        model = MeterRequest
        fields = '__all__'