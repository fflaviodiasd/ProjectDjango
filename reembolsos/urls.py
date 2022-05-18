from django.conf import settings
from django.contrib import admin
from django.urls import URLPattern, path, include
from django.conf.urls.static import static

from . import views

admin.site.site_header = 'Admin Sys - NAF'
admin.site.site_title = 'Admin Sys - NAF'
admin.site.index_title = 'Administração do Sistema'

urlpatterns = [
    path('', views.index, name='index'),
    path('reembolso', views.reembolso, name='reembolso'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
