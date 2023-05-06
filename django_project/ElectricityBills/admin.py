from django.contrib import admin
from .models import Payment,MeterRequest,PayBills,LicenseRequest,ReconciliationRequest
# Register your models here.
admin.site.register(Payment)
admin.site.register(MeterRequest)
admin.site.register(PayBills)
admin.site.register(LicenseRequest)
admin.site.register(ReconciliationRequest)