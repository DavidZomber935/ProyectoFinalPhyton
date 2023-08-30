from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('',views.index, name="index"),
    path('shop/',views.shop,name="shop"),
    path('productDetails/',views.productDetails,name="productDetails"),
    path('contact/',views.contact,name="contact"),
    path('admin/', admin.site.urls),
]
