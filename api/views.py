from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class VocabularyAPIView(APIView):
    def get(self, requeest):
        return Response('{vocab: "Greeting", means: "ทักทาย"}')
