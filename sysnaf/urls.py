from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', include('reembolsos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),

    re_path(r'^$', views.IndexView.as_view(), name="index_url"),

    path('users/', include('users.urls', namespace="users")),
]
