from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context

# Create your views here.

def getcharts(req):
 
   t=loader.get_template('chart.html')
   c=Context({})
   return HttpResponse(t.render(c))

