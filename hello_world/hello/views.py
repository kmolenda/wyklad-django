from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home_who(request, who):
    # str_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # str_welcome = f"<h1>Hello <b>{who}</b>!</h1><br> Now is {str_now}!"

    # # sql = f"SELECT * FROM table WHERE name = {who}"

    # return HttpResponse( str_welcome ) #+ "<br>" + sql )
    return render(
        request, 
        'hello/index_who.html',     # nazwa szablonu
        {                           # słownik zmiennych
            'who': who,
            'now': datetime.now()
        }
    )