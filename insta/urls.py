from django.urls import path
from .import views


#urls
urlpatterns = [
    path('',views.loginPage, name="login"),
    path('register/',views.registerPage, name="register"),
    path('insta/', views.insta, name='insta'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_post, name='search.post'), 
    path('like/', views.like_image, name='like-image'),
    path('comments/<image_id>', views.comments,name='comments'),
]