from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import InvoiceForm
from .models import Invoice

def dashboard(request):
    invoices = Invoice.objects.filter(created_by=request.user)
    context = {
        "invoices" : invoices,
        "title" : "Dashboard"
    }
    return render(request, "dashboard.html", context)


def create_invoice(request):
    # Handles the creation of an invoice
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.created_by = request.user
            invoice.save()
            return redirect(reverse("invoice:detail", invoice.id))
    else: 
        form = InvoiceForm()
        
    context = {
        "form" : form,
        "title" : "Create an invoice",
    }
    
    return render(request, "invoice_form.html", context)

def update_invoice(request, invoice_id):
    # Handles the update of an invoice
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == "POST":
        form = InvoiceForm(request.post, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect("invoice:detail", invoice.id)
        else:
            form = InvoiceForm(instance=invoice)
        
        context = {
            "form" : form,
            #"invoice" : invoice,
            "title" : "Edit the invoice"
        }
    return render(request, "invoice_form.html", context)

def delete_invoice(request, invoice_id):
    # Handles the deletion of an invoice
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if request.method == "POST":
        invoice.delete()
        return redirect("invoice:dashboard")
    context = {
        "title" : "Delete the Invoice",
    }
    return render(request, "confirm_delete.html", context)

def detail_invoice(request, invoice_id):
    # Displays an invoice details
    invoice = get_object_or_404(Invoice, id=invoice_id)
    context={
        "title" : "Invoice details"
    }
    return render(request, "invoice_details.html", context)
    