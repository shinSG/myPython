from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
# Create your views here.

def index(req):
    #eturn HttpResponse("<h1>Welcome To My Zone</h1>")
	t = loader.get_template('index.html')
	c=Context({})
	return HttpResponse(t.render(c))
