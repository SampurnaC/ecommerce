from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static

app_name='store'


urlpatterns = [
    path('', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product_detail, name='product-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
