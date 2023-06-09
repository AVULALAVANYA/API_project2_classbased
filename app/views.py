from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import*
from app.serializer import *
from rest_framework.response import Response
class ProductCrud(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)
    def post(self,request):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'massage':'prodict id created'})
        return Response({'failed':'product is created'})

    def put(self,request):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'product is update'})
        return Response({'failed':'product is update'})
        



