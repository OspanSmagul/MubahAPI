from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from companies.models import Company 
from companies.serializers import CompanySerializer

from django.db.models import Q
from rest_framework import generics, mixins

from django.contrib import messages
 
class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs) 
 
 
@csrf_exempt 
def company_list(request): 
    if request.method == 'GET': 
        company = Company.objects.all() 
        c_serializer = CompanySerializer(company, many=True) 
        return JSONResponse(c_serializer.data) 
 
    elif request.method == 'POST': 
        c_data = JSONParser().parse(request) 
        c_serializer = CompanySerializer(data=c_data, many=True) 
        if c_serializer.is_valid(): 
            c_serializer.save() 
            return JSONResponse(c_serializer.data,
            status=status.HTTP_201_CREATED) 
        return JSONResponse(c_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST) 
 
 
@csrf_exempt 
def company_detail(request, pk): 
    try: 
        company = Company.objects.get(pk=pk) 
    except Company.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        c_serializer = CompanySerializer(company) 
        return JSONResponse(c_serializer.data) 
 
    elif request.method == 'PUT': 
        c_data = JSONParser().parse(request) 
        c_serializer = CompanySerializer(company, data=c_data) 
        if c_serializer.is_valid(): 
            c_serializer.save() 
            return JSONResponse(c_serializer.data) 
        return JSONResponse(c_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        company.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class CompanyAPIView(mixins.CreateModelMixin, generics.ListAPIView):  
    lookup_field = 'pk'
    serializer_class = CompanySerializer
    #queryset = Products.objects.all()

    def get_queryset(self):
        qs = Company.objects.all()
        query=self.request.GET.get("q")
        
        if query is not None:
            qs = qs.filter(
                    Q(company_name__icontains=query)|
                    Q(brand_name__icontains=query))   
        # else:
        #   qs = "There are no such a product. But we will add it soon. Thank you!"
        return qs

    def perform_create(self, serializer):
        serializer.save(barcode=self.request.barcode)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CompanyRudView(generics.RetrieveUpdateDestroyAPIView):  #DetailView  CreareView FormView
    lookup_field = 'pk'
    serializer_class = CompanySerializer
    #queryset = Products.objects.all()

    def get_queryset(self):
        return Company.objects.all()