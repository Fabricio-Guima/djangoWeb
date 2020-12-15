from django.contrib import admin
from django.urls import path, include
from .views import teste
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste),
    path('', include('website.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
