from django.shortcuts import render
from rest_framework.views import APIView # importing from the django rest_framework.views
from rest_framework.response import Response # to send back response
from drfapp.serializers import StudentSerializer
from drfapp.models import Student


class TesView(APIView):
     # GET METHOD fn
    def get(self, request, *args, **kwargs):
        # data = {
        #     'name':'admin',
        #     'email': 'admin@gmail.com',
        #     'age': 10
        # }
        # serializing data in a get request
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True) # many=True means it is more than one
        return Response(serializer.data)
    
    # POST METHOD fn
    def post(self, request, *args, **kwargs):
         # the data=request.data is added because we want to submit something and get the the data passed to the APIView but if you are not submitting anything, you can just serializer = StudentSerializer
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(): # checking if all the field values are correct
            serializer.save()
            return Response(serializer.data) # returnin g a response of the particular data the user save
        return Response(serializer.errors)