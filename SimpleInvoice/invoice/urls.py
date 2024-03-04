from django.urls import path
from . import views

app_name = "invoice"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create/", views.create_invoice, name="create"),
    path("delete/<uuid:invoice_id>/", views.delete_invoice, name="delete"),
    path("detail/<uuid:invoice_id>/", views.detail_invoice, name="detail"),
    path("update/<uuid:invoice_id>/", views.update_invoice, name="update"),
    
]
 