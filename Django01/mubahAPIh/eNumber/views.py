from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from eNumber.models import eNumber 
from eNumber.serializers import eNumberSerializer 
 
from django.db.models import Q
from rest_framework import generics, mixins

from django.contrib import messages
 
class JSONResponse(HttpResponse): 
    def __init__(self, data, **kwargs): 
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json' 
        super(JSONResponse, self).__init__(content, **kwargs) 
 
 
@csrf_exempt 
def eNumber_list(request): 
    if request.method == 'GET': 
        e = eNumber.objects.all() 
        e_serializer = eNumberSerializer(e, many=True) 
        return JSONResponse(e_serializer.data) 
 
    elif request.method == 'POST': 
        e_data = JSONParser().parse(request) 
        e_serializer = eNumberSerializer(data=e_data) 
        if e_serializer.is_valid(): 
            e_serializer.save() 
            return JSONResponse(e_serializer.data,
            status=status.HTTP_201_CREATED) 
        return JSONResponse(e_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST) 
 
 
@csrf_exempt 
def eNumber_detail(request, pk): 
    try: 
        e = eNumber.objects.get(pk=pk) 
    except eNumber.DoesNotExist: 
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        e_serializer = eNumberSerializer(e) 
        return JSONResponse(e_serializer.data) 
 
    elif request.method == 'PUT': 
        e_data = JSONParser().parse(request) 
        e_serializer = eNumberSerializer(e, data=e_data) 
        if e_serializer.is_valid(): 
            e_serializer.save() 
            return JSONResponse(e_serializer.data) 
        return JSONResponse(e_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        e.delete() 
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class eNumberAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = eNumberSerializer
    #queryset = Products.objects.all()

    def get_queryset(self):
        qs = eNumber.objects.all()
        query=self.request.GET.get("q")

        if query is not None:
            qs = qs.filter(
                    Q(number__iexact=query)|
                    Q(id__iexact=query))   
        #else:
        #   qs = "There are no such a product. But we will add it soon. Thank you!"
        return qs

    def perform_create(self, serializer):
        serializer.save(number=self.request.number)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class eNumberRudView(generics.RetrieveUpdateDestroyAPIView):  #DetailView  CreareView FormView
    lookup_field = 'pk'
    serializer_class = eNumberSerializer
    #queryset = Products.objects.all()

    def get_queryset(self):
        return eNumber.objects.all()