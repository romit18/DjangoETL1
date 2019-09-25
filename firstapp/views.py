from django.shortcuts import render

from django.views.generic import CreateView
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

from . import forms
def index(request):
  return render(request, 'index.html')

def services(request):
  return render(request,'services.html')

def signup(request):
  if request.method=="POST":
    form = forms.UserCreateForm(request.POST)
    if form.is_valid():
      user=form.save()
      username=form.cleaned_data.get("username")
      email=form.cleaned_data.get("email")
      login(request,user)
      return redirect('index')
    else:
      for msg in form.error_messages:
        print(form.error_messages[msg])

      return render(request = request,
                          template_name = "registration/signup.html",
                          context={"form":form})
  form=forms.UserCreateForm
  return render(request,'registration/signup.html',{'form': form})

  def Login(request):
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        user = authenticate(request, username = username, password = password) 
        if user is not None: 
            form = login(request, user) 
            messages.success(request, f' Welcome {username} !!') 
            return redirect('index') 
        else: 
            messages.info(request, f'account done not exit please sign in') 
    form = AuthenticationForm() 
    return render(request, 'registration/login.html', {'form':form, 'title':'log in'}) 

def about(request):
  return render(request, 'trailers.html')

def about1(request):
  return render(request, 'sacred.html')


def about2(request):
  return render(request, 'shark.html')

def epi(request):
  return render(request, 'episodes.html')
