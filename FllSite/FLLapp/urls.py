from django.conf.urls import url
from . import views
app_name='FLLapp'
urlpatterns=[
        url(r'^$', views.index, name="index"),
        url(r'^aboutcenter(?P<centerid>[0-9]+)/',views.aboutcenter,name="aboutcenter"),
        url(r'^searchresults',views.searchresults,name="searchresults"),
        url(r'^search$',views.search,name='search'),
        url(r'^aboutlab(?P<labid>[0-9]+)/',views.aboutlab,name="aboutlab"),
        url(r'^animal(?P<animalid>[0-9]+)/',views.animal,name="animal")
]

