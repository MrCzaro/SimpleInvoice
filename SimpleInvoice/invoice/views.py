from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from fpdf import FPDF
from .forms import InvoiceForm
from .models import Invoice


@login_required
def dashboard(request):
    invoices = Invoice.objects.filter(created_by=request.user)
    context = {"invoices": invoices, "title": "Dashboard"}
    return render(request, "dashboard.html", context)


@login_required
def create_invoice(request):
    # Handles the creation of an invoice
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.created_by = request.user
            invoice.save()
            return redirect("invoice:detail", invoice.id)
    else:
        form = InvoiceForm()
    back_url = reverse("invoice:dashboard")
    context = {"form": form, "title": "Create an invoice", "url": back_url}

    return render(request, "invoice_form.html", context)


@login_required
def update_invoice(request, invoice_id):
    # Handles the update of an invoice
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect("invoice:detail", invoice.id)
    else:
        form = InvoiceForm(instance=invoice)
    back_url = reverse("invoice:detail", args=[invoice.id])
    context = {
        "form": form,
        "invoice": invoice,
        "title": "Edit the invoice",
        "url": back_url,
    }
    return render(request, "invoice_form.html", context)


@login_required
def create_similar_invoice(request, invoice_id):
    # Handles the creation of a similar invoice
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == "POST":
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            new = form.save(commit=False)
            new.id = None
            new.save()
            return redirect("invoice:detail", invoice.id)
    else:
        form = InvoiceForm(instance=invoice)
    back_url = reverse("invoice:detail", args=[invoice.id])
    context = {
        "form": form,
        "invoice": invoice,
        "title": "Create a smilar invoice",
        "url": back_url,
    }
    return render(request, "invoice_form.html", context)


@login_required
def delete_invoice(request, invoice_id):
    # Handles the deletion of an invoice
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == "POST":
        invoice.delete()
        return redirect("invoice:dashboard")
    context = {"title": "Delete the Invoice", "invoice": invoice}
    return render(request, "confirm_delete.html", context)


@login_required
def detail_invoice(request, invoice_id):
    # Displays an invoice details
    invoice = get_object_or_404(Invoice, id=invoice_id)
    back_url = reverse("invoice:dashboard")
    context = {"invoice": invoice, "title": "Invoice details", "url": back_url}
    return render(request, "invoice_details.html", context)


@login_required
def download_invoice(request, invoice_id):
    # Handles creation of invoice in pdf format and make it downloadable
    invoice = get_object_or_404(Invoice, id=invoice_id)

    # Generate the PDF content
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break("auto")

    # Invoice number
    pdf.set_font("Helvetica", "B", size=18)
    pdf.text(10, 10, f"Invoice number: {invoice.invoice_number}")

    # Place of creation, date of issue, and date of service:
    pdf.set_font("Helvetica", "B", size=10)

    # Place of creation
    pdf.text(145, 30, f"Place of creation: {invoice.place_of_creation}")

    # Date of issue:
    pdf.text(145, 35, f"Date of issue: {invoice.date_of_creation.strftime('%Y-%m-%d')}")

    # Date of service
    pdf.text(
        145, 40, f"Date of service: {invoice.date_of_service.strftime('%Y-%m-%d')}"
    )

    # Seller:
    pdf.set_font("helvetica", "B", size=12)
    pdf.text(20, 75, "Seller details:")
    pdf.set_font("helvetica", size=10)

    company_y_position = 80
    pdf.text(20, company_y_position, f"{invoice.company_name}")
    pdf.text(20, company_y_position + 5, f"{invoice.company_street_address}")
    pdf.text(20, company_y_position + 10, f"{invoice.company_city}")
    pdf.text(20, company_y_position + 15, f"{invoice.company_zip_code}")
    pdf.text(20, company_y_position + 20, f"{invoice.company_tax_id}")
    pdf.text(20, company_y_position + 25, f"{invoice.company_phone}")

    # Customer:
    pdf.set_font("helvetica", "B", size=12)
    pdf.text(120, 75, "Customer details:")
    pdf.set_font("helvetica", size=10)

    customer_y_position = 80
    pdf.text(120, customer_y_position, f"{invoice.customer_company_name}")
    pdf.text(120, customer_y_position + 5, f"{invoice.customer_street_address}")
    pdf.text(120, customer_y_position + 10, f"{invoice.customer_city}")
    pdf.text(120, customer_y_position + 15, f"{invoice.customer_zip_code}")
    pdf.text(120, customer_y_position + 20, f"{invoice.customer_tax_id}")
    pdf.text(120, customer_y_position + 25, f"{invoice.customer_phone}")

    # Service type:

    pdf.set_font("helvetica", "B", size=12)
    pdf.text(15, 150, "Service type:")

    service_type_y_position = 155
    pdf.set_font("helvetica", size=10)
    pdf.text(15, service_type_y_position, f"{invoice.service_type_1}")
    if len(invoice.service_type_2) > 1:
        service_type_y_position += 5
        pdf.text(15, service_type_y_position, f"{invoice.service_type_2}")
    if len(invoice.service_type_3) > 1:
        service_type_y_position += 5
        pdf.text(15, service_type_y_position, f"{invoice.service_type_3}")

    # Unit:

    pdf.set_font("helvetica", "B", size=12)
    pdf.text(90, 150, "Unit:")

    unit_y_position = 155
    pdf.set_font("helvetica", size=10)
    pdf.text(90, unit_y_position, f"{invoice.unit_1.capitalize()}")
    if len(invoice.unit_2) > 1:
        unit_y_position += 5
        pdf.text(90, unit_y_position, f"{invoice.unit_2.capitalize()}")
    if len(invoice.unit_3) > 1:
        unit_y_position += 5
        pdf.text(90, unit_y_position, f"{invoice.unit_3.capitalize()}")

    # Amount:
    pdf.set_font("helvetica", "B", size=12)
    pdf.text(115, 150, "Amount:")

    amount_y_position = 155
    pdf.set_font("helvetica", size=10)
    pdf.text(115, amount_y_position, f"{invoice.amount_1}")
    if invoice.amount_2 is not None:
        amount_y_position += 5
        pdf.text(115, amount_y_position, f"{invoice.amount_2}")
    if invoice.amount_3 is not None:
        amount_y_position += 5
        pdf.text(115, amount_y_position, f"{invoice.amount_3}")

    # Price:
    pdf.set_font("helvetica", "B", size=12)
    pdf.text(145, 150, "Price:")

    price_y_position = 155
    pdf.set_font("helvetica", size=10)
    pdf.text(145, price_y_position, f"{invoice.price_1}")
    if invoice.price_2 is not None:
        price_y_position += 5
        pdf.text(145, price_y_position, f"{invoice.price_2}")
    if invoice.price_3 is not None:
        price_y_position += 5
        pdf.text(145, price_y_position, f"{invoice.price_3}")

    # Total price:
    pdf.set_font("helvetica", "B", size=12)
    pdf.text(170, 150, "Total price:")

    total_price_y_position = 155
    pdf.set_font("helvetica", size=10)
    pdf.text(170, total_price_y_position, f"{invoice.total_price_1}")
    if invoice.total_price_2 is not None:
        total_price_y_position += 5
        pdf.text(170, total_price_y_position, f"{invoice.total_price_2}")
    if invoice.total_price_3 is not None:
        total_price_y_position += 5
        pdf.text(170, total_price_y_position, f"{invoice.total_price_3}")

    # Total due:
    pdf.set_font("helvetica", "B", size=10)
    pdf.text(20, 190, f"Total due: ")
    pdf.set_font("helvetica", size=10)
    pdf.text(38, 190, f"{invoice.total_price} {invoice.currency}")
    # Account number:
    pdf.set_font("helvetica", "B", size=10)
    pdf.text(20, 195, f"Account number: ")
    pdf.set_font("helvetica", size=10)
    pdf.text(50, 195, f"{invoice.company_account_number}")

    # Method payment:
    pdf.set_font("helvetica", "B", size=10)
    pdf.text(20, 200, f"Method payment: ")
    pdf.set_font("helvetica", size=10)
    pdf.text(50, 200, f"{invoice.method_payment}")

    # Due date:
    pdf.set_font("helvetica", "B", size=10)
    pdf.text(20, 205, "Due date: ")
    pdf.set_font("helvetica", size=10)
    pdf.text(36, 205, "14 days")

    # Comments:
    if len(invoice.additional_information) > 1:
        pdf.text(70, 240, f"Comments: {invoice.additional_information}")

    # Seller singature:
    pdf.set_font("helvetica", "B", size=8)
    pdf.text(20, 270, "Seller signature:")
    pdf.text(20, 275, "-----------------")

    # Buyer signature:
    pdf.text(150, 270, "Buyer signature:")
    pdf.text(150, 275, "----------------")
    # Output the PDF content
    response = HttpResponse(content_type="application/pdf")
    response[
        "Content-Disposition"
    ] = f"attachment; filename='invoice_{invoice.invoice_number}.pdf'"

    pdf_output = pdf.output(dest="S").encode("latin-1")
    response.write(pdf_output)

    return response
