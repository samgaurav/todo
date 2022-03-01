from django.shortcuts import render ,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate , login as loginUser, logout #its method to check if user authenticate or not
from . forms import TODOForm
from . models import TODO
from django.contrib.auth.decorators import login_required #its a decorator this will give access of home page after login

@login_required(login_url='login') # becoz of decorator when ur not login this home page will redirected to login page
def home(request):
    if request.user.is_authenticated:
        user = request.user #by this two steps we will get login user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('priority')#order_by shows priority at ascending order
        #todos = TODO.objects.filter(user = user).order_by('-priority') #order_by shows priority at decsending order prefix "-"
        #  #its show only login user todos
        #when we apply condition we use filter
        #"""todos = TODO.objects.all()=>its shows all users to do"""
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos , 'user_name' : user.username  })
        #'user_name' : user.username --> it will show the login user name in UI side after that go to index.html
        #<h1>Welcome {{user_name}}</h1>


def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )

        """What does cleaned_data mean in Django? cleaned_data returns a dictionary of validated form 
                   input fields and their values, where string primary keys are returned as objects"""
        """Difference between cleaned_data and cleaned_data.get in Django is that if the key does not
         exist in the dictionary, self.cleaned_data[‘field’] will raise a KeyError,
          while self.cleaned_data.get(‘field’) will return None."""


def signup(request):

    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context=context)

@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else:
            return render(request , 'index.html' , context={'form' : form})


def delete_todo(request , id ): #integer id we required primary key(here id is pk)
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('home') #after delete it goes home page

def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id) #by this get method we will get object of that id
    todo.status = status #we sets the status params
    todo.save()
    return redirect('home')

def signout(request):
    logout(request)
    return redirect('login')#after logout it will redirect to login, login its a name give at urls.py path
#if thier is not name then we cannt redrict



