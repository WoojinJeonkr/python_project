from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def start(request):
    return HttpResponse('리턴되었습니다.')