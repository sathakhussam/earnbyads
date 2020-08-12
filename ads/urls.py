from django.urls import path
from . import views
urlpatterns = [
    path('ads',views.ads_page,name='ads_page')
]