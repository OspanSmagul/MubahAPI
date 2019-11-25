from django.conf.urls import url 
from companies import views 
 

from .views import CompanyRudView
from .views import CompanyAPIView

app_name = 'companies'

urlpatterns = [ 
    # url(r'^company/$', views.company_list), 
    # url(r'^company/(?P<pk>[0-9]+)/$', views.company_detail), 
    url(r'^$', CompanyAPIView.as_view(), name='company-create'),
    url(r'^(?P<pk>\d+)/$', CompanyRudView.as_view(), name='company-rud') 
] 