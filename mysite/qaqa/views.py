#!/usr/bin/python3
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import json


def index(request):
    template = loader.get_template('qaqa/templates/qaqa/index.html')
    # views_list =  {"name":"菜鸟教程","age":18}
    with open('qaqa/check_ok.txt', "r") as fs:
        json_url = fs.read()
        fs.close()

    list_url = json.loads(json_url)
        

    return HttpResponse(template.render({"list_url": list_url}, request))