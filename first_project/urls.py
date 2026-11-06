from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('media/', media),
    path('about/', about),
    path('contact/', contact),
    path('services/', services),
    path('portfolio/', portfolio),
]