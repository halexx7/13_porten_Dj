import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('product/', mainapp.product, name='product'),
    path("product/man", mainapp.product, name="product_man"),
    path("product/woman", mainapp.product, name="product_woman"),
    path("product/kids", mainapp.product, name="product_kids"),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    