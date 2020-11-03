from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('qaqa/', include('qaqa.urls')),
    path('admin/', admin.site.urls),
]