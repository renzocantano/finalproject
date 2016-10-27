from django.conf.urls import  url
from django.contrib import admin
from jeepney import views
from .views import(
    jeepneys_list,
    jeepneys_create,
    jeepneys_detail,
    jeepneys_updated,
    jeepneys_delete,
)

urlpatterns = [
    url(r'^$', jeepneys_list, name='list'),
    url(r'^(?P<id>\d+)/$',jeepneys_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$',jeepneys_updated, name='updated'),
    url(r'^(?P<id>\d+)/delete/$', jeepneys_delete, name='delete'),
]
