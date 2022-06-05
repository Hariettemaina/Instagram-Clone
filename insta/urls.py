from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('timeline/',views.timeline,name = 'timeline'),
    path('accounts/profile/',views.profile,name = 'profile'),
    path('accounts/create',views.create,name = 'create'),
    path('accounts/search',views.search,name = 'search'),
    path('accounts/updateProfile',views.updateProfile,name = 'updateProfile'),
    path('accounts/single/',views.single,name = 'single'),
    path('like/',views.likePost,name= 'likePost'),
	path('follow/',views.follow,name="user_follow"),
	path('editPost/',views.editPost,name="editPost"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)