from django.urls import path,include
from .views import Hv,Sv
from .models import City

urlpatterns = [
    path ('',Hv.as_view(),name='home'),
    path ('search',Sv.as_view(),name='search'),
]

