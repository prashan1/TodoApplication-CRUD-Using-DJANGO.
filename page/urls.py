from django.urls import path
from django.contrib.auth import views as authview
from . import views
urlpatterns =[
	path('',views.todoList.as_view(),name='todolist'),	
	path('tododetail/<int:pk>/',views.todoDetail.as_view(),name='tododetail'),
	path('todoupdate/<int:pk>/',views.todoUpdate.as_view(),name='todoupdate'),
	path('tododelete/<int:pk>/',views.todoDelete.as_view(),name='tododelete'),
	path('create-task/',views.todoCreate.as_view(),name='todocreate'),
	path('login/',views.CustomLoginView.as_view(),name='login'),
	path('logout/',authview.LogoutView.as_view(next_page='login'),name='logout'),
	path('register/',views.RegisterPage.as_view(),name='register'),

]