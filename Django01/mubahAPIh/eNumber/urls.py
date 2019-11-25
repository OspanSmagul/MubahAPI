from django.conf.urls import url 
from eNumber import views 
 
from .views import eNumberRudView
from .views import eNumberAPIView

app_name = 'eNumber'

urlpatterns = [ 
    # url(r'^eNumber/$', views.eNumber_list), 
    # url(r'^eNumber/(?P<pk>[0-9]+)/$', views.eNumber_detail), 
    url(r'^$', eNumberAPIView.as_view(), name='eNumber-create'),
    url(r'^(?P<pk>\d+)/$', eNumberRudView.as_view(), name='eNumber-rud') 
] 