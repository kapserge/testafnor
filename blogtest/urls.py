from django.urls import path, include
from django.conf.urls import url 
from rest_framework.routers import DefaultRouter
from . import views
from .views import detailApiView
    
router = DefaultRouter()


urlpatterns = [
    url(r'^api/(?P<pk>[0-9]+)/$', detailApiView.as_view({'get': 'get'}), name="get_single"),
    url(r'^api/$', detailApiView.as_view({'get': 'list_obf'}), name="obf_list")]
