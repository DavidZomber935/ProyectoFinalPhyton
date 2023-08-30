from django.shortcuts import render

# Create your views here.
htmlBase="""
    <h1>Mi Web</h1>
    <ul>
        <li><a href="/">index</a></li>
        <li><a href="/shop">Tienda</a></li>
        <li><a href="/productDetails">Detalles del Producto</a></li>
        <li><a href="/contact">Contacto</a></li>
    </ul>
"""

def index(request):
    return render(request, "core/index.html")

def shop(request):
    return render(request, "core/shop.html")

def productDetails(request):
     return render(request, "core/productDetails.html")

def contact(request):
    return render(request, "core/contact.html")