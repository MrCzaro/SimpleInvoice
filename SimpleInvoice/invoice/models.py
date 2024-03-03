import uuid

from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


CURRENCY_CHOICES = (
    ("PLN", 'Polish Zloty (PLN)'),
    ("EUR", 'Euro (EUR)'),
    ("GBP", 'British Pound Sterling (GBP)'),
    ("CHF", 'Swiss Franc (CHF)'),
    ("SEK", 'Swedish Krona (SEK)'),
    ("NOK", 'Norwegian Krone (NOK)'),
    ("DKK", 'Danish Krone (DKK)'),
    ("HUF", 'Hungarian Forint (HUF)'),
    ("CZK", 'Czech Koruna (CZK)'),
    ("RON", 'Romanian Leu (RON)'),
    ('USD', 'US Dollar (USD)'),
)

METHOD_PAYMENT_CHOICES = (
    ("money transfer", "Money transfer"),
    ("cash", "CASH"),
)

UNIT_CHOICES = (
    ("hours", "HOURS"),
    ("days", "DAYS"),
    ("quantity", "QUANTITY"),
    ("units", "UNITS"),
    ("pieces", "PIECES"),
)

class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Invoice details:
    place_of_creation = models.CharField(max_length=100)
    date_of_creation = models.DateField()
    date_of_service = models.DateField()
    invoice_number = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(max_length=50, choices=CURRENCY_CHOICES)
    method_payment = models.CharField(max_length=20, choices=METHOD_PAYMENT_CHOICES)
    service_type_1 = models.CharField(max_length=100)
    service_type_2 = models.CharField(max_length=100, blank=True)
    service_type_3 = models.CharField(max_length=100, blank=True)
    unit_1 = models.CharField(max_length=15, choices=UNIT_CHOICES)
    unit_2 = models.CharField(max_length=15, choices=UNIT_CHOICES, blank=True)
    unit_3 = models.CharField(max_length=15, choices=UNIT_CHOICES, blank=True)
    price_1 = models.DecimalField(max_digits=100, decimal_places=2, validators=[MinValueValidator(0)])
    price_2 = models.DecimalField(max_digits=100, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True)
    price_3 = models.DecimalField(max_digits=100, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True)
    amount_1 = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    amount_2 = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True)
    amount_3 = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True)
    total_price_1 = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    total_price_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_price_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    # Company details:
    company_name = models.CharField(max_length=255)
    company_street_address = models.CharField(max_length=255)
    company_city = models.CharField(max_length=100)
    company_zip_code = models.CharField(max_length=50)
    company_tax_id = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=20)
    company_account_number = models.CharField(max_length=50, blank=True)
    # Customer details:
    customer_company_name = models.CharField(max_length=255)
    customer_street_address = models.CharField(max_length=255)
    customer_city = models.CharField(max_length=100)
    customer_zip_code = models.CharField(max_length=50)
    customer_tax_id = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["-created_at"]

        
    def __str__(self):
        return f"(Invoice Number: {self.invoice_number})"


    def save(self, *args, **kwargs):
        # Calculate total_price 1 which is mandatory:
        self.total_price_1 = self.price_1 * self.amount_1
        self.total_price = self.total_price_1
        # Calculate total_price_2 and total_price_3 whih are not mandatory
        if self.price_2 and self.amount_2:
            self.total_price_2 = self.price_2 * self.amount_2
            self.total_price += self.total_price_2
        if self.price_3 and self.amount_3:
            self.total_price_3 = self.price_3 * self.amount_3
            self.total_price += self.total_price_3

        # Save calculations:
        super().save(*args, **kwargs)