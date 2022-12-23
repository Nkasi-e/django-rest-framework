from django.shortcuts import render
from rest_framework.views import APIView # importing from the django rest_framework.views
from rest_framework.response import Response # to send back response


class TesView(APIView):
     # get fn
    def get(self, request, *args, **kwargs):
        data = {
            'name':'admin',
            'email': 'admin@gmail.com',
            'age': 10
        }
        return Response(data)