from django.contrib import admin
from django.urls import path, include
# from apis.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('apis/', include(router.urls)),
    path('api/', include('apis.urls')),
]
