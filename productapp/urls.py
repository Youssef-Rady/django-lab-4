from django.urls import path 
from productapp.views import homepage, contactus, aboutus, showproduct, deleteproduct, createNewProduct, editProduct
from django.contrib.auth.decorators import login_required

urlpatterns = [ 
    path('home', homepage, name='home'),
    path('contact', contactus, name='contactus'),
    path('about', aboutus, name='aboutus'),
    path('show/<int:id>', showproduct, name='show'),
    path('delete/<int:id>', deleteproduct, name='delete'),
    path('create', login_required(createNewProduct), name='create'),
    path('edit/<int:id>', editProduct, name='edit')

    ]

