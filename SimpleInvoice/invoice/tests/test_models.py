from django.test import TestCase

from invoice.models import Invoice
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

class InvoiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
        username='test_user',
        email='test@django.com',
        password='test_user_password',
        )
        cls.invoice = Invoice.objects.create(
            created_by = cls.user,
            place_of_creation="Company City",
            date_of_creation="2024-03-03",
            date_of_service="2024-03-03",
            invoice_number="INV-2024-03-01",
            currency="PLN",
            method_payment="money transfer",
            service_type_1="Service 1",
            unit_1="hours",
            price_1=100.00,
            amount_1=5,
            service_type_2="Service 2",
            unit_2="units",
            price_2=200.00,
            amount_2=4,
            company_name="Company",
            company_street_address="Company Street",
            company_city="Company City",
            company_zip_code="12345A",
            company_tax_id="0987654321",
            company_phone="+1234567890",
            customer_company_name="Customer Company",
            customer_street_address="Customer Street",
            customer_city="Customer City",
            customer_zip_code="12345B",
            customer_tax_id="1234567890",            
        )
    
    def test_valid_invoice(self):
        self.assertEqual(self.invoice.place_of_creation, "Company City")
        self.assertEqual(self.invoice.created_by, self.user)
        self.assertEqual(self.invoice.date_of_creation, "2024-03-03")
        self.assertEqual(self.invoice.date_of_service, "2024-03-03")
        self.assertEqual(self.invoice.invoice_number, "INV-2024-03-01")
        self.assertEqual(self.invoice.currency, "PLN")
        self.assertEqual(self.invoice.method_payment, "money transfer")
        self.assertEqual(self.invoice.service_type_1, "Service 1")
        self.assertEqual(self.invoice.unit_1, "hours")
        self.assertEqual(self.invoice.price_1, 100.00)
        self.assertEqual(self.invoice.amount_1, 5)
        self.assertEqual(self.invoice.unit_2, "units")
        self.assertEqual(self.invoice.company_name, "Company")
        self.assertEqual(self.invoice.customer_company_name, "Customer Company")
        self.assertEqual(self.invoice.company_street_address, "Company Street")
        self.assertEqual(self.invoice.customer_street_address, "Customer Street")
        self.assertEqual(self.invoice.customer_tax_id, "1234567890")
        self.assertEqual(self.invoice.company_tax_id, "0987654321")
        self.assertEqual(self.invoice.company_city, "Company City")
        self.assertEqual(self.invoice.customer_city, "Customer City")
        self.assertEqual(self.invoice.company_zip_code, "12345A")
        self.assertEqual(self.invoice.customer_zip_code, "12345B")
        self.assertEqual(self.invoice.company_phone, "+1234567890")
        self.assertEqual(self.invoice.total_price_1, 500)
        self.assertEqual(self.invoice.total_price_2, 800)
        self.assertEqual(self.invoice.total_price, 1300)
        
    
    def test_place_of_creation_label(self):
        field_label = self.invoice._meta.get_field("place_of_creation").verbose_name
        self.assertEqual(field_label, "place of creation")
        
    def test_date_of_creation_label(self):
        field_label = self.invoice._meta.get_field("date_of_creation").verbose_name
        self.assertEqual(field_label, "date of creation")
    
    def test_date_of_service_label(self):
        field_label = self.invoice._meta.get_field("date_of_service").verbose_name
        self.assertEqual(field_label, "date of service")
        
    def test_invoice_number_label(self):
        field_label = self.invoice._meta.get_field("invoice_number").verbose_name
        self.assertEqual(field_label, "invoice number")
        
    def test_created_by_label(self):
        field_label = self.invoice._meta.get_field("created_by").verbose_name
        self.assertEqual(field_label, "created by")
    
    def test_created_at_label(self):
        field_label = self.invoice._meta.get_field("created_at").verbose_name
        self.assertEqual(field_label, "created at")
        
    def test_modified_at_label(self):
        field_label = self.invoice._meta.get_field("modified_at").verbose_name
        self.assertEqual(field_label, "modified at")
        
    def test_currency_label(self):
        field_label = self.invoice._meta.get_field("currency").verbose_name
        self.assertEqual(field_label, "currency")
    
    def test_method_payment_label(self):
        field_label = self.invoice._meta.get_field("method_payment").verbose_name
        self.assertEqual(field_label, "method payment")
        
    def test_service_type_1_label(self):
        field_label = self.invoice._meta.get_field("service_type_1").verbose_name
        self.assertEqual(field_label, "service type 1")
        
    def test_service_type_2_label(self):
        field_label = self.invoice._meta.get_field("service_type_2").verbose_name
        self.assertEqual(field_label, "service type 2")
        
    def test_service_type_3_label(self):
        field_label = self.invoice._meta.get_field("service_type_3").verbose_name
        self.assertEqual(field_label, "service type 3")
        
    def test_unit_1_label(self):
        field_label = self.invoice._meta.get_field("unit_1").verbose_name
        self.assertEqual(field_label, "unit 1")
        
    def test_unit_2_label(self):
        field_label = self.invoice._meta.get_field("unit_2").verbose_name
        self.assertEqual(field_label, "unit 2")
        
    def test_unit_3_label(self):
        field_label = self.invoice._meta.get_field("unit_3").verbose_name
        self.assertEqual(field_label, "unit 3")
    
    def test_price_1_label(self):
        field_label = self.invoice._meta.get_field("price_1").verbose_name
        self.assertEqual(field_label, "price 1")
        
    def test_price_2_label(self):
        field_label = self.invoice._meta.get_field("price_2").verbose_name
        self.assertEqual(field_label, "price 2")
        
    def test_price_3_label(self):
        field_label = self.invoice._meta.get_field("price_3").verbose_name
        self.assertEqual(field_label, "price 3")
        
    def test_amount_1_label(self):
        field_label = self.invoice._meta.get_field("amount_1").verbose_name
        self.assertEqual(field_label, "amount 1")
    
    def test_amount_2_label(self):
        field_label = self.invoice._meta.get_field("amount_2").verbose_name
        self.assertEqual(field_label, "amount 2")
        
    def test_amount_3_label(self):
        field_label = self.invoice._meta.get_field("amount_3").verbose_name
        self.assertEqual(field_label, "amount 3")

    def test_total_price_1_label(self):
        field_label = self.invoice._meta.get_field("total_price_1").verbose_name
        self.assertEqual(field_label, "total price 1")
        
    def test_total_price_2_label(self):
        field_label = self.invoice._meta.get_field("total_price_2").verbose_name
        self.assertEqual(field_label, "total price 2")
        
    def test_total_price_3_label(self):
        field_label = self.invoice._meta.get_field("total_price_3").verbose_name
        self.assertEqual(field_label, "total price 3")
        
    def test_total_price_label(self):
        field_label = self.invoice._meta.get_field("total_price").verbose_name
        self.assertEqual(field_label, "total price")
    
    def test_company_name_label(self):
        field_label = self.invoice._meta.get_field("company_name").verbose_name
        self.assertEqual(field_label, "company name")
        
    def test_company_street_address_label(self):
        field_label = self.invoice._meta.get_field("company_street_address").verbose_name
        self.assertEqual(field_label, "company street address")

    def test_company_city_label(self):
        field_label = self.invoice._meta.get_field("company_city").verbose_name
        self.assertEqual(field_label, "company city")
        
    def test_company_zip_code_label(self):
        field_label = self.invoice._meta.get_field("company_zip_code").verbose_name
        self.assertEqual(field_label, "company zip code")

    def test_company_tax_id_label(self):
        field_label = self.invoice._meta.get_field("company_tax_id").verbose_name
        self.assertEqual(field_label, "company tax id")
        
    def test_company_phone_label(self):
        field_label = self.invoice._meta.get_field("company_phone").verbose_name
        self.assertEqual(field_label, "company phone")
    
    def test_company_account_number_label(self):
        field_label = self.invoice._meta.get_field("company_account_number").verbose_name
        self.assertEqual(field_label, "company account number")
        
    def test_customer_company_name_label(self):
        field_label = self.invoice._meta.get_field("customer_company_name").verbose_name
        self.assertEqual(field_label, "customer company name")

    def test_customer_street_address_label(self):
        field_label = self.invoice._meta.get_field("customer_street_address").verbose_name
        self.assertEqual(field_label, "customer street address")
        
    def test_customer_city_label(self):
        field_label = self.invoice._meta.get_field("customer_city").verbose_name
        self.assertEqual(field_label, "customer city")

    def test_customer_zip_code_label(self):
        field_label = self.invoice._meta.get_field("customer_zip_code").verbose_name
        self.assertEqual(field_label, "customer zip code")
        
    def test_customer_tax_id_label(self):
        field_label = self.invoice._meta.get_field("customer_tax_id").verbose_name
        self.assertEqual(field_label, "customer tax id")
        
    def test_save_method(self):
        invoice = Invoice.objects.create(
            created_by = self.user,
            place_of_creation="Company City",
            date_of_creation="2024-03-03",
            date_of_service="2024-03-03",
            invoice_number="INV-2024-03-01",
            currency="PLN",
            method_payment="money transfer",
            service_type_1="Service 1",
            unit_1="hours",
            price_1=100.00,
            amount_1=5,
            service_type_2="Service 2",
            unit_2="units",
            price_2=200.00,
            amount_2=4,
            company_name="Company",
            company_street_address="Company Street",
            company_city="Company City",
            company_zip_code="12345A",
            company_tax_id="0987654321",
            company_phone="+1234567890",
            customer_company_name="Customer Company",
            customer_street_address="Customer Street",
            customer_city="Customer City",
            customer_zip_code="12345B",
            customer_tax_id="1234567890",            
        )
        invoice.save()
        self.assertIsNotNone(invoice.total_price_1)
        self.assertIsNotNone(invoice.total_price_2)
        self.assertIsNotNone(invoice.total_price)
        self.assertIsNone(invoice.total_price_3)

    def test_string_representation(self):
        # Test the __str__ representation
        expected_str = f"(Invoice Number: {self.invoice.invoice_number})"
        self.assertEqual(str(self.invoice), expected_str)

        
