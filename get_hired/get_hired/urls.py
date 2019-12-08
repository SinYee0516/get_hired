from django.urls import path

from django.urls import path
from django.contrib import admin
from app import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('user/', views.UserList.as_view()),
]

"""
    path('user/', views.UserList.as_view()),
    path('job/', views.JobList.as_view()),
    path('company/', views.CompanyList.as_view()),
    path('status/', views.StatusList.as_view()),
    path('message/', views.MessageList.as_view()),
    path('saved/', views.SavedList.as_view()),
   
    path('user_post/user_post_list/', user_post_list, name='post'),"""