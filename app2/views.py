from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista3(request):
    html="""
    <h1>Estás en la vista 3</h1>
"""
    return HttpResponse(html)

def vista4(request):
    html="""
    <h1>Estás en la vista 4</h1>
"""
    return HttpResponse(html)