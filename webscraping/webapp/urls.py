from django.urls import path
from webapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('reload',views.scrapear,name='reload'),
]
