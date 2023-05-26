import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
# Create your views here.

def main(request): # Главная страница
    
    #Колличество посещений этого view, подсчитанное в переменой session
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Отрисовка HTML-шаблона index.html с данными
    # внутри переменной index
    return render (request,'main/index.html',
                   context={
                            'title':'Главная страница',
                            'num_visits': num_visits},
                   )

def _toJson(data, method = 0): # 0 если один объект, 1 если более
    if method == 0:
        returns = json.dumps(data.as_json(), ensure_ascii=False).encode('utf-8')
    elif method == 1:
        returns = [] # список в котором находятся все json-объекты
        for i in data:
            returns.append(i)
        returns = json.dumps(returns, ensure_ascii=False).encode('utf-8')
    return returns


# def test(request):
#     data = Seans.objects.get(pk=request.GET['id'])
#     return HttpResponse(_toJson(data), content_type="application/json")


def test(request):
    data = Seans.objects.all()
    response = [ob.as_json() for ob in data] 
    result_json = _toJson(response,1)
    return HttpResponse(result_json, content_type="application/json")
    




        
    