from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework import status  

#generic
from django.db.models import Q
from rest_framework import generics, mixins

from django.contrib import messages

from products.models import Products
from .serializers import ProductsSerializer 


class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs) 
 
 
@csrf_exempt 
def products_list(request): 
    if request.method == 'GET': 
        products = Products.objects.all() 
        products_serializer = ProductSerializer(products, many=True) 
        return JSONResponse(products_serializer.data) 
 
    elif request.method == 'POST': 
        product_data = JSONParser().parse(request) 
        product_serializer = ProductSerializer(data=product_data) 
        if products_serializer.is_valid(): 
            products_serializer.save() 
            return JSONResponse(products_serializer.data,
            status=status.HTTP_201_CREATED) 
        return JSONResponse(products_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST) 
 
 
@csrf_exempt 
def products_detail(request, pk): 
    try: 
        products = Products.objects.get(pk=barcode) 
    except Products.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        products_serializer = ProductSerializer(products) 
        return JSONResponse(products_serializer.data) 
 
    elif request.method == 'PUT': 
        product_data = JSONParser().parse(request) 
        products_serializer = ProductSerializer(products, data=product_data) 
        if products_serializer.is_valid(): 
            products_serializer.save() 
            return JSONResponse(products_serializer.data) 
        return JSONResponse(products_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        products.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class ProductsAPIView(mixins.CreateModelMixin, generics.ListAPIView):  #DetailView  CreareView FormView
	lookup_field = 'pk'
	serializer_class = ProductsSerializer
	#queryset = Products.objects.all()

	def get_queryset(self):
		qs = Products.objects.all()
		query=self.request.GET.get("q")
		
		if query is not None:
			qs = qs.filter(
					Q(barcode__iexact=query)| 
					Q(name__icontains=query))	
		# else:
		# 	qs = "There are no such a product. But we will add it soon. Thank you!"
		return qs

	def perform_create(self, serializer):
		serializer.save(barcode=self.request.barcode)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class ProductsRudView(generics.RetrieveUpdateDestroyAPIView):  #DetailView  CreareView FormView
	lookup_field = 'pk'
	serializer_class = ProductsSerializer
	#queryset = Products.objects.all()

	def get_queryset(self):
		return Products.objects.all()

	# def get_object(self): 
	# 	pk=self.kwargs.get("pk")
	# 	return Products.objects.get(pk=pk)

