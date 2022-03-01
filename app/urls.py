from django.contrib import admin
from django.urls import path
from .views import *
#from .views import home,login,signup
urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('signup', signup, name = "signup"),
    path('add-todo/', add_todo), #my mistake  path('add_todo', add_todo, name = "add_todo"), underscore
    path('delete-todo/<int:id>' , delete_todo ),
    path('change-status/<int:id>/<str:status>' , change_todo ),#<int:id> its a dynamic value its changes when
    # we delete specify object we need id when we perform edit and delete
    path('logout/' , signout ),
]
