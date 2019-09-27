
from django.conf.urls import url, include
# from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('krish.urls', namespace='krish')),
    url(r'^tinymce/', include('tinymce.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
