from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.


def main(request):
  return HTTPResponse('<h1> HOLAAAAA </h1>')