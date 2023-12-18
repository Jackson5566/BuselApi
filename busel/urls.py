from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product_app.urls')),
    path('api/', include('contact_app.urls')),
    path('api/', include('auth_app.urls')),
]
