
from django.conf.urls import url
from . import views

app_name = 'tree'

urlpatterns = [
    #/tree/HomePage
    url(r'^$', views.IndexView.as_view(), name='index'),

    #tree/register/  For registartion of the users
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/tree/Person
    url(r'persons/$', views.PersonView.as_view(), name='persons'),


    #/tree/family/add
    url(r'family/add/$', views.FamilyCreate.as_view(), name='family_add'),
    #/tree/person/add
    url(r'person/add/$', views.PersonCreate.as_view(), name='person_add'),


    #/tree/family/
    url(r'family/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/tree/person/2/
    url(r'persons/(?P<pk>[0-9]+)/$', views.DetailPersonView.as_view(), name='person_detail'),


    #/tree/family/3/
    url(r'family/(?P<pk>[0-9]+)/update$', views.FamilyUpdate.as_view(), name='family_update'),
    #/tree/person/2/update
    url(r'persons/(?P<pk>[0-9]+)/update$', views.PersonUpdate.as_view(), name='person_update'),


    #/tree/family/2/delete/
    url(r'family/(?P<pk>[0-9]+)/delete/$', views.FamilyDelete.as_view(), name='family_delete'),
    #/tree/family/2/delete/
    url(r'persons/(?P<pk>[0-9]+)/delete/$', views.PersonDelete.as_view(), name='person_delete'),









]
