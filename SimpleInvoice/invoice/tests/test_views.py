from django.test import TestCase
from django.urls import reverse
import uuid

from accounts.models import CustomUser
from invoice.models import Invoice

class DashboardViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
        username="test@django.com",
        email="test@django.com",
        password="test_user_password123",
        )
    
    def test_authentication_required(self):
        response = self.client.get(reverse("invoice:dashboard"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,"/accounts/login/?next=/")
        
    def test_successful_rendering(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard.html")
        
    def test_context_data(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("invoices", response.context)
        self.assertIn("title", response.context)
        
class CreateInvoiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
        username="test@django.com",
        email="test@django.com",
        password="test_user_password123",
        )
        
    def test_authentication_required(self):
        response = self.client.get(reverse("invoice:create"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,"/accounts/login/?next=/create/")
        
    def test_successful_rendering(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "invoice_form.html")
        
    def test_context_data(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:create"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertIn("title", response.context)
        self.assertIn("url", response.context)
        
    def test_form_submission_valid_data(self):
        data = {
            "created_by" : self.user,
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
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.post(reverse("invoice:create"), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("invoice:detail", args=[Invoice.objects.first().id]))
        self.assertEqual(Invoice.objects.count(), 1)
        
    def test_form_submission_invalid_data(self):
        data = {
            "created_by" : self.user,
            "place_of_creation" : "Company City",
            "date_of_creation" : "2024-03-03",
            "date_of_service" : "2024-03-03",
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
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.post(reverse("invoice:create"), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "invoice_form.html")
        self.assertEqual(Invoice.objects.count(), 0)
        
class UpdateInvoiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
        username="test@django.com",
        email="test@django.com",
        password="test_user_password123",
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
            customer_phone="213721"            
        )
        
    def test_authentication_required(self):
        response = self.client.get(reverse("invoice:update", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/update/{self.invoice.id}/")
        
    def test_successful_rendering(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:update", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "invoice_form.html")
        
    def test_context_data(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:update", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertIn("invoice", response.context)
        self.assertIn("title", response.context)
        self.assertIn("url", response.context)
        
    def test_form_submission(self):
        data = {
            "created_by" : self.user,
            "place_of_creation" : "Company City",
            "date_of_creation" : "2024-03-03",
            "date_of_service" : "2024-03-03",
            "invoice_number" : "INV-2024-03-01",
            "currency" : "PLN",
            "method_payment" : "money transfer",
            "service_type_1" : "Service 1 Edited",
            "unit_1" : "hours",
            "price_1" : 100.00,
            "amount_1" : 5,
            "service_type_2" : "Service 2 Edited",
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
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.post(reverse("invoice:update", args=[self.invoice.id]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("invoice:detail", args=[self.invoice.id]))
        updated_invoice = Invoice.objects.get(id=self.invoice.id)
        self.assertEqual(updated_invoice.service_type_1, "Service 1 Edited")
        self.assertEqual(updated_invoice.service_type_2, "Service 2 Edited")
        
        
class CreateSimilarInvoiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
        username="test@django.com",
        email="test@django.com",
        password="test_user_password123",
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
            customer_phone="213721"            
        )
        
    def test_authentication_required(self):
        response = self.client.get(reverse("invoice:create-similar", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/create-similar/{self.invoice.id}/")
        
    def test_successful_rendering(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:create-similar", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "invoice_form.html")
        
    def test_context_data(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:create-similar", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertIn("invoice", response.context)
        self.assertIn("title", response.context)
        self.assertIn("url", response.context)
        
    def test_form_submission_valid_data(self):        
        data = {
            "created_by" : self.user,
            "place_of_creation" : "Company City",
            "date_of_creation" : "2024-03-06",
            "date_of_service" : "2024-03-06",
            "invoice_number" : "INV-2024-03-06/2",
            "currency" : "PLN",
            "method_payment" : "money transfer",
            "service_type_1" : "Service 1 copy",
            "unit_1" : "hours",
            "price_1" : 100.00,
            "amount_1" : 5,
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
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        # One instance of the invoice in the data base before form submission
        self.assertEqual(Invoice.objects.count(), 1)
        response = self.client.post(reverse("invoice:create-similar", args=[self.invoice.id]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("invoice:detail", args=[Invoice.objects.first().id]))
        # Two instances of the invoice in the data base after  form submission
        self.assertEqual(Invoice.objects.count(), 2)
        
    def test_form_submission_invalid_data(self):
        data = {
            "created_by" : self.user,
            "place_of_creation" : "Company City",
            "date_of_creation" : "2024-03-03",
            "date_of_service" : "2024-03-03",
            "company_name" : "Company",
            # "company_street_address" : "Company Street",
            # "company_city" : "Company City",
            # "company_zip_code" : "12345A",
            # "company_tax_id" : "0987654321",
            # "company_phone" : "+1234567890",
            "customer_company_name" : "Customer Company",
            "customer_street_address" : "Customer Street",
            "customer_city" : "Customer City",
            "customer_zip_code" : "12345B",
            "customer_tax_id" : "1234567890",
            "customer_phone" : "213721"  
        }
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.post(reverse("invoice:create-similar", args=[self.invoice.id]), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "invoice_form.html")
        self.assertEqual(Invoice.objects.count(), 1)
        
class DeleteInvoiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
        username="test@django.com",
        email="test@django.com",
        password="test_user_password123",
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
            customer_phone="213721"            
        )
        
    def test_authentication_required(self):
        response = self.client.get(reverse("invoice:delete", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/delete/{self.invoice.id}/")
        
    def test_successful_rendering(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:delete", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "confirm_delete.html")
        
    def test_context_data(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:delete", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("invoice", response.context)
        self.assertIn("title", response.context)
    
    def test_patient_deletion(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.post(reverse("invoice:delete", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("invoice:dashboard"))
        with self.assertRaises(Invoice.DoesNotExist):
            Invoice.objects.get(id=self.invoice.id)
            
class Detail_InvoiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
        username="test@django.com",
        email="test@django.com",
        password="test_user_password123",
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
            customer_phone="213721"            
        )
        
    def test_authentication_required(self):
        response = self.client.get(reverse("invoice:detail", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/detail/{self.invoice.id}/")
        
    def test_successful_rendering(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:detail", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "invoice_details.html")
        
    def test_context_data(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:detail", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("invoice", response.context)
        self.assertIn("title", response.context)
        self.assertIn("url", response.context)
        
    def test_back_url(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:detail", args=[self.invoice.id]))
        back_url = response.context["url"]
        self.assertEqual(back_url, reverse("invoice:dashboard"))
        

class DownloadInvoiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
        username="test@django.com",
        email="test@django.com",
        password="test_user_password123",
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
            customer_phone="213721"            
        )
    def test_authentication_required(self):
        response = self.client.get(reverse("invoice:download", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next=/download/{self.invoice.id}/")
        
    def test_invoice_not_found(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:download", args=[uuid.uuid4()]))
        self.assertEqual(response.status_code, 404)
        
    def test_download_invoice(self):
        self.client.login(username="test@django.com", email="test@django.com",password="test_user_password123")
        response = self.client.get(reverse("invoice:download", args=[self.invoice.id]))
        self.assertEqual(response.status_code, 200)
        # Check that the response is a PDF
        self.assertEqual(response["Content-Type"], "application/pdf")

        # Check that the filename in Content-Disposition matches the expected format
        expected_filename = f"invoice_{self.invoice.invoice_number}.pdf"
        self.assertEqual(response["Content-Disposition"], f"attachment; filename='{expected_filename}'")