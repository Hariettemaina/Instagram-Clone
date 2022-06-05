from turtle import title
from django.shortcuts import render,redirect
from .models import Image,Comment,Profile,User,Follow
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
#from .forms import NewImagePost,CreateComment,UpdateProfile
from .models import Image,Comment,Profile,User,Follow
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST





# Create your views here.
def index(request):
	'''
	Method that fetches all images from all users.
	'''
	images = Image.objects.all()
	title = "Discover"
	
	return render(request,'index.html',{"images":images,"title":title})

def timeline(request):
	'''
	Method that fetches imges from all the users that the current logged in user follows only
	'''
	follows = Follow.objects.filter(user_from = request.user.id)
	images = Image.objects.filter(profile = request.user.following.user_to)
	return render(request, 'accounts/timeline.html',{"images":images,"title":title})