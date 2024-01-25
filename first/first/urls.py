from django.contrib import admin
from django.urls import path
from ombor.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('bosh/', bosh_sahifa),
    path('ob/', ob_havo),
    path('jadval/',hamma_kitoblar),
]
