from products import views 

from .views import ProductsRudView
from .views import ProductsAPIView
from django.conf.urls import url

app_name = 'products'

urlpatterns = [
	# url(r'^api/products/$', views.product_list), 
    # url(r'^api/products/(?P<pk>[0-9]+)/$', views.product_detail),
	url(r'^$', ProductsAPIView.as_view(), name='product-create'),
    url(r'^(?P<pk>\d+)/$', ProductsRudView.as_view(), name='product-rud') 
]
