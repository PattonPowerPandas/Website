from django.conf.urls import url
from . import views
app_name='FLLapp'
urlpatterns=[
        url(r'^$', views.index, name="index"),
        url(r'^aboutcenter(?P<centerid>[0-9]+)/',views.aboutcenter,name="aboutcenter"),
        url(r'^searchresults',views.searchresults,name="searchresults"),
        url(r'^search$',views.search,name='search'),
        url(r'^aboutlab(?P<labid>[0-9]+)/',views.aboutlab,name="aboutlab"),
        url(r'^animal(?P<animalid>[0-9]+)/',views.animal,name="animal"),
        url(r'^animalsearch/',views.animalsearch,name="animalsearch"),
        url(r'^animalsearchresults/',views.animalsearchresults,name="animalsearchresults"),
        url(r'^about/',views.about,name="about"),
        url(r'^contact/',views.contact,name="contact"),
        url(r'^donate/',views.donate,name="donate"),
        url(r'^laws/',views.laws,name="laws"),
]

