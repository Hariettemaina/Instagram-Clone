from django.shortcuts import render,redirect
from .models import Image,Comment,Profile,User,Follow




# Create your views here.
def index(request):
	'''
	Method that fetches all images from all users.
	'''
	images = Image.objects.all()
	title = "Discover"
	
	return render(request,'index.html',{"images":images,"title":title})