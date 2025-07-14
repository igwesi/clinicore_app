from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('', include('apps.accounts.urls')),
    path('staff/', include('apps.staff.urls')),
    path('patient/', include('apps.patients.urls')),
    path('clinic/', include('apps.clinic_app.urls')),
    
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
]
# from django.conf.urls import handler404, handler500
# if not settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

settings.DEBUG = False