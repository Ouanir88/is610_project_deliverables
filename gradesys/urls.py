from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grading/', include('grading.urls')),
    path('reports/', include('reports.urls')),
    
]