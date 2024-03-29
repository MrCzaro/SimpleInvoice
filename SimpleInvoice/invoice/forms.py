from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice

        fields = [
            "place_of_creation",
            "date_of_creation",
            "date_of_service",
            "invoice_number",
            "currency",
            "method_payment",
            "service_type_1",
            "service_type_2",
            "service_type_3",
            "unit_1",
            "unit_2",
            "unit_3",
            "price_1",
            "price_2",
            "price_3",
            "amount_1",
            "amount_2",
            "amount_3",
            "additional_information",
            "company_name",
            "company_street_address",
            "company_city",
            "company_zip_code",
            "company_tax_id",
            "company_phone",
            "company_account_number",
            "customer_company_name",
            "customer_street_address",
            "customer_city",
            "customer_zip_code",
            "customer_tax_id",
            "customer_phone",
        ]

        labels = {
            "place_of_creation": "Place Of Issue",
            "date_of_creation": "Date Of Issue",
            "date_of_service": "Date Of Service",
            "invoice_number": "Invoice Number",
            "currency": "Currency",
            "method_payment": "Method Of Payment",
            "service_type_1": "Name Of Sercive",
            "unit_1": "Unit",
            "price_1": "Price",
            "amount_1": "Quantity",
            "company_name": "Company Name",
            "company_street_address": "Street Address",
            "company_city": "City",
            "company_zip_code": "Zip Code",
            "company_tax_id": "Tax Id",
            "company_phone": "Telephone Number",
            "company_account_number": "Account Number",
            "customer_company_name": "Company Name",
            "customer_street_address": "Street Address",
            "customer_city": "City",
            "customer_zip_code": "Zip Code",
            "customer_tax_id": "Tax Id",
            "customer_phone": "Telephone Number",
            "additional_information": "Additional Information",
        }

        widgets = {
            "place_of_creation": forms.TextInput(attrs={"class": "form-class"}),
            "date_of_creation": forms.DateInput(
                attrs={"type": "date", "class": "form-class"}
            ),
            "date_of_service": forms.DateInput(
                attrs={"type": "date", "class": "form-class"}
            ),
            "invoice_number": forms.TextInput(attrs={"class": "form-class"}),
            "currency": forms.Select(attrs={"class": "form-class"}),
            "method_payment": forms.Select(attrs={"class": "form-class"}),
            "service_type_1": forms.TextInput(
                attrs={"class": "form-class", "placeholder": "1"}
            ),
            "service_type_2": forms.TextInput(
                attrs={"class": "form-class", "placeholder": "2"}
            ),
            "service_type_3": forms.TextInput(
                attrs={"class": "form-class", "placeholder": "3"}
            ),
            "unit_1": forms.Select(attrs={"class": "form-class"}),
            "unit_2": forms.Select(attrs={"class": "form-class"}),
            "unit_3": forms.Select(attrs={"class": "form-class"}),
            "price_1": forms.NumberInput(attrs={"class": "form-class"}),
            "price_2": forms.NumberInput(attrs={"class": "form-class"}),
            "price_3": forms.NumberInput(attrs={"class": "form-class"}),
            "amount_1": forms.NumberInput(attrs={"class": "form-class"}),
            "amount_2": forms.NumberInput(attrs={"class": "form-class"}),
            "amount_3": forms.NumberInput(attrs={"class": "form-class"}),
            "additional_information": forms.Textarea(
                attrs={"class": "form-class", "rows": 1}
            ),
            "company_name": forms.TextInput(attrs={"class": "form-class"}),
            "company_street_address": forms.TextInput(attrs={"class": "form-class"}),
            "company_city": forms.TextInput(attrs={"class": "form-class"}),
            "company_zip_code": forms.TextInput(attrs={"class": "form-class"}),
            "company_tax_id": forms.TextInput(attrs={"class": "form-class"}),
            "company_phone": forms.TextInput(attrs={"class": "form-class"}),
            "company_account_number": forms.TextInput(attrs={"class": "form-class"}),
            "customer_company_name": forms.TextInput(attrs={"class": "form-class"}),
            "customer_street_address": forms.TextInput(attrs={"class": "form-class"}),
            "customer_city": forms.TextInput(attrs={"class": "form-class"}),
            "customer_zip_code": forms.TextInput(attrs={"class": "form-class"}),
            "customer_tax_id": forms.TextInput(attrs={"class": "form-class"}),
            "customer_phone": forms.TextInput(attrs={"class": "form-class"}),
        }
