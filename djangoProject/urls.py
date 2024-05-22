from django.contrib import admin
from django.urls import path, include  # Ensure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('my_app.urls')),  # Include URLs from 'my_app'
]
