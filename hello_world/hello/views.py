from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home_who(request, who):
    str_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    str_welcome = f"Hello <b>{who}</b>!<br> Now is {str_now}!"

    return HttpResponse( str_welcome )