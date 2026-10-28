from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^product/(?P<product_id>\d+)/$', views.product_view, name='product'),
    re_path(r'^product/(?P<product_id>.+)/$', views.product_view, name='product_invalid'),  
    re_path(r'^product/$', views.product_view, name='product_no_id'),
]
