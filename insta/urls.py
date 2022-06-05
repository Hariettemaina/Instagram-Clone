from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('^$',views.index,name = 'index'),
    path('^timeline/$',views.timeline,name = 'timeline'),
    path(r'^accounts/profile/(\d+)',views.profile,name = 'profile'),
    path(r'^accounts/create',views.create,name = 'create'),
    path(r'^accounts/search',views.search,name = 'search'),
    path(r'^accounts/updateProfile',views.updateProfile,name = 'updateProfile'),
    path(r'^accounts/single/(\d+)',views.single,name = 'single'),
    path(r'^like/(\d+)',views.likePost,name= 'likePost'),
	path(r'^follow/(\d+)',views.follow,name="user_follow"),
	path(r'^editPost/(\d+)',views.editPost,name="editPost"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)