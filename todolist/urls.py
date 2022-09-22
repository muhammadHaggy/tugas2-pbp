from django.urls import path
from .views import logout_user, register, login_user, show_todolist, add_task
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('create-task/', add_task, name='add_task'),
]
