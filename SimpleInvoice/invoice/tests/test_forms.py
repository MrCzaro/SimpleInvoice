from django.test import TestCase

from accounts.models import CustomUser
from invoice.forms import InvoiceForm
from invoice.models import Invoice

class InvoiceFromTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
        username="test@django.com",
        email="test@django.com",
        password="test_user_password123",
        )
    
    def test_form_initialization(self):
        form = InvoiceForm()
        self.assertIsInstance(form, InvoiceForm)
        
    def test_valid_form(self):
        data = {
            "place_of_creation" : "Company City",
            "date_of_creation" : "2024-03-03",
            "date_of_service" : "2024-03-03",
            "invoice_number" : "INV-2024-03-01",
            "currency" : "PLN",
            "method_payment" : "money transfer",
            "service_type_1" : "Service 1",
            "unit_1" : "hours",
            "price_1" : 100.00,
            "amount_1" : 5,
            "service_type_2" : "Service 2",
            "unit_2" : "units",
            "price_2" : 200.00,
            "amount_2" : 4,
            "company_name" : "Company",
            "company_street_address" : "Company Street",
            "company_city" : "Company City",
            "company_zip_code" : "12345A",
            "company_tax_id" : "0987654321",
            "company_phone" : "+1234567890",
            "customer_company_name" : "Customer Company",
            "customer_street_address" : "Customer Street",
            "customer_city" : "Customer City",
            "customer_zip_code" : "12345B",
            "customer_tax_id" : "1234567890",
            "customer_phone" : "213721"  
        }
        form = InvoiceForm(data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        # Empty form
        data = {}
        form = InvoiceForm(data)
        self.assertFalse(form.is_valid())
        
        # Missing fields
        data = {
            #"place_of_creation" : "Company City",
            "date_of_creation" : "2024-03-03",
            "date_of_service" : "2024-03-03",
            #"invoice_number" : "INV-2024-03-01",
            "currency" : "PLN",
            "method_payment" : "money transfer",
            "service_type_1" : "Service 1",
            "unit_1" : "hours",
            "price_1" : 100.00,
            "amount_1" : 5,
            "amount_2" : 4,
            "company_name" : "Company",
            "company_street_address" : "Company Street",
            #"company_city" : "Company City",
            "company_zip_code" : "12345A",
            "company_tax_id" : "0987654321",
            "company_phone" : "+1234567890",
            "customer_company_name" : "Customer Company",
            #"customer_street_address" : "Customer Street",
            "customer_city" : "Customer City",
            "customer_zip_code" : "12345B",
            "customer_tax_id" : "1234567890",
            "customer_phone" : "213721"  
        }
        form = InvoiceForm(data)
        self.assertFalse(form.is_valid())
        
    def test_save_method(self):
        data = {
            "place_of_creation" : "Company City",
            "date_of_creation" : "2024-03-03",
            "date_of_service" : "2024-03-03",
            "invoice_number" : "INV-2024-03-01",
            "currency" : "PLN",
            "method_payment" : "money transfer",
            "service_type_1" : "Service 1",
            "unit_1" : "hours",
            "price_1" : 100.00,
            "amount_1" : 5,
            "service_type_2" : "Service 2",
            "unit_2" : "units",
            "price_2" : 200.00,
            "amount_2" : 4,
            "company_name" : "Company",
            "company_street_address" : "Company Street",
            "company_city" : "Company City",
            "company_zip_code" : "12345A",
            "company_tax_id" : "0987654321",
            "company_phone" : "+1234567890",
            "customer_company_name" : "Customer Company",
            "customer_street_address" : "Customer Street",
            "customer_city" : "Customer City",
            "customer_zip_code" : "12345B",
            "customer_tax_id" : "1234567890",
            "customer_phone" : "213721"  
        }
        form = InvoiceForm(data)
        self.assertTrue(form.is_valid())
        
        invoice = form.save(commit=False)
        invoice.created_by = self.user
        invoice.save()
        self.assertIsInstance(invoice, Invoice)
        
    
    def test_place_of_creation_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["place_of_creation"].label, "Place Of Issue")
        
    def test_date_of_creation_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["date_of_creation"].label, "Date Of Issue")
        
    def test_date_of_service_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["date_of_service"].label, "Date Of Service")
        
    def test_currency_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["currency"].label, "Currency")
        
    def test_method_payment_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["method_payment"].label, "Method Of Payment")
        
    def test_service_type_1_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["service_type_1"].label, "Name Of Sercive")

    def test_unit_1_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["unit_1"].label, "Unit")
        
    def test_price_1_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["price_1"].label, "Price")
        
    def test_amount_1_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["amount_1"].label, "Quantity")
        
    def test_company_name_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["company_name"].label, "Company Name")
        
    def test_company_street_address_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["company_street_address"].label, "Street Address")
        
    def test_company_city_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["company_city"].label, "City")
    
    def test_company_zip_code_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["company_zip_code"].label, "Zip Code")
        
    def test_company_tax_id_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["company_tax_id"].label, "Tax Id")
        
    def test_company_phone_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["company_phone"].label, "Telephone Number")
        
    def test_company_account_number_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["company_account_number"].label, "Account Number")
        
    def test_customer_company_name_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["customer_company_name"].label, "Company Name")
        
    def test_customer_street_address_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["customer_street_address"].label, "Street Address")
        
    def test_customer_city_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["customer_city"].label, "City")
        
    def test_customer_zip_code_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["customer_zip_code"].label, "Zip Code")
        
    def test_customer_tax_id_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["customer_tax_id"].label, "Tax Id")
        
    def test_customer_phone_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["customer_phone"].label, "Telephone Number")
        
    def test_additional_information_label(self):
        form = InvoiceForm()
        self.assertEqual(form.fields["additional_information"].label, "Additional Information")