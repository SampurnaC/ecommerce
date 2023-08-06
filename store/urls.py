from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static
from .forms import LoginForm
from django.contrib.auth import views as auth_views

app_name='store'


urlpatterns = [
    path('', views.products, name='products'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product_detail, name='product-detail'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
