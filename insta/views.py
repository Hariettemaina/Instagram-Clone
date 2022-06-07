from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .models import posts,Likes,Comment,Profile
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,UserCreationForm,CommentForm
from django.shortcuts import render,redirect, get_object_or_404

from insta.forms import CreateUserForm
from .models import posts #import photos model

def insta(request):
    # imports photos and save it in database
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
    photo = posts.objects.all().order_by('-id')
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'temps/insta.html', ctx)
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
			
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)  
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('insta')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)  
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    # get images for the current logged in user
    image = posts.objects.filter(user_id=current_user.id)
    # get the profile of the current logged in user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm (request.POST , request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        redirect('profile')
    return render(request, 'temps/profile.html', {"image": image, "profile": profile , "form": form})
    
@login_required(login_url='/accounts/login/')
def search_post(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = posts.search_image_name(search_term)
        message = f'{search_term}'

        return render(request, 'all-photos/search.html', {'found': message, 'images': images})
    else:
        message = 'Not found'
        return render(request, 'all-photos/search.html', {'danger': message})
    
def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_pic =posts.objects.get(id=image_id)
        if user in image_pic.liked.all():
            image_pic.liked.add(user)
        else:
            image_pic.liked.add(user)    
            
        like,created =Likes.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value =='Like':
               like.value = 'Dislike'
        else:
               like.value = 'Like'

        like.save()       
    return redirect('insta')

@login_required
def comments(request,image_id):
  form = CommentForm()
  image = posts.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('insta')    