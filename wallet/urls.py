from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = 'wallet'

urlpatterns = [

    #/wallet/HomePage
    url(r'^$', views.index, name='index'),

    #/wallet/73
    url(r'^(?P<category_id>[0-9]+)/$', views.category_detail, name='category_detail'),


]