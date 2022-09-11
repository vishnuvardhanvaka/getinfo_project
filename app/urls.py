from django.urls import path
from . import views
urlpatterns=[
path('',views.home),
path('mobile/',views.mobile),
path('laptop/',views.laptop),
path('tv/',views.tv)
]

