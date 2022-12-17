

# Django
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


# Views
from front.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
    path('api/v1/auth/', include('accounts.urls')),
    path('',index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
