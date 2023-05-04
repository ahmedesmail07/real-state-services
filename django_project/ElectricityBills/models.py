from django.db import models
from django import forms
class Payment(models.Model):
    codenumber = models.CharField(max_length=20)
    meterreding = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image/')
    comments = models.TextField()

    def __str__(self):
        return self.codenumber

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['codenumber', 'meterreding', 'company', 'comments',]