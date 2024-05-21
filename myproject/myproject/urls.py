from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views
from myapp.views import NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView


urlpatterns = [
    path('', NoteListView.as_view(), name='home'), # main page, class view
    path('admin/', admin.site.urls), 
    path('new/', NoteCreateView.as_view(), name='create-note'),
    path('update/<int:pk>', NoteUpdateView.as_view(), name='update-note'), # <int:pk>: note id
    path('delete/<int:pk>', NoteDeleteView.as_view(), name='delete-note'),
    path('register/', views.register, name='register'), # Function view
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
]

