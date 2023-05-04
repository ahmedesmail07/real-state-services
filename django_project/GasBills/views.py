from django.shortcuts import render
from django.contrib import messages
from .models import ProvideGasMeter, NaturalGasReading


def form_six(request):
    if request.method == 'POST':
        name = request.POST.get("full-name")
        national_identity_card_number = request.POST.get("national-id")
        national_identity_card_photo = request.POST.get("national-id-image")
        copy_of_the_ownership_contract = request.POST.get(
            "property-contract-image")
        photo_of_recent_electricity_receipt = request.POST.get(
            "electricity-receipt-image")
        receipt_of_approval_from_gas_company = request.POST.get(
            "property-image")
        origin_type = request.POST.get("facility-type")

        # Perform validation
        if not name:
            messages.error(request, 'Please provide a name.')
        elif not national_identity_card_number:
            messages.error(
                request, 'Please provide a national identity card number.')
        # Add more validation conditions as needed

        # If there are no validation errors, save the data
        if not messages.get_messages(request):
            new_bill = NaturalGasReading(
                name=name,
                national_identity_card_number=national_identity_card_number,
                national_identity_card_photo=national_identity_card_photo,
                copy_of_the_ownership_contract=copy_of_the_ownership_contract,
                photo_of_recent_electricity_receipt=photo_of_recent_electricity_receipt,
                receipt_of_approval_from_gas_company=receipt_of_approval_from_gas_company,
                origin_type=origin_type
            )
            new_bill.save()
            return render(request, 'GasBills/form6.html')

    return render(request, 'GasBills/form6.html')


def form_seven(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        national_identity_card_number = request.POST.get("national-id")
        last_reading = request.POST.get("last-reading")
        last_reading_date = request.POST.get("date")
        current_reading = request.POST.get("current-reading")
        counter_image = request.POST.get("image")
        origin_type = request.POST.get("type")

        # Perform validation
        if not name:
            messages.error(request, 'Please provide a name.')
        elif not national_identity_card_number:
            messages.error(
                request, 'Please provide a national identity card number.')
        # Add more validation conditions as needed

        # If there are no validation errors, save the data
        if not messages.get_messages(request):
            new_reading = NaturalGasReading(
                name=name,
                national_identity_card_number=national_identity_card_number,
                last_reading=last_reading,
                last_reading_date=last_reading_date,
                current_reading=current_reading,
                counter_image=counter_image,
                origin_type=origin_type
            )
            new_reading.save()
            return render(request, 'GasBills/form7.html')

    return render(request, 'GasBills/form7.html')
