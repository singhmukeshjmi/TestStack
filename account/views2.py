from django.forms import ValidationError
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .custompermissions import OnePermission
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

#UserModel = get_user_model()

# def profileview(request,pk):
#     if request.method == 'POST':
#         form = profileform(request.POST)
#         if form.is_valid:
#             print(form)
#             form.save()
#         else:
#             print("Not valid")
#         return render(request, "form.html", {'form' : form})
#     else:
#         instance = User.objects.get(pk=pk)
#         form = profileform(instance=instance)
#         print(form)
#         return render(request, "accounts/profileview.html", {'form' : form})
    
class UserUpdateView(UpdateView):
   model=User
   fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login']
   template_name='accounts/profileview.html'
   #permission_classes = [OnePermission,]
   success_url='/'


class UserDetailView(DetailView):
    model=User
    fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login']
    template_name='accounts/profiledetailview.html'
#    success_url='/'


def mainpage(request):
    print('redirecting to homepage')
    return redirect('homepage')
from .forms2 import profileform
def myprofileedit(request):
    user = request.user
    user = User.objects.get(pk=user.id)
    form = profileform(instance=user)
    if request.method == 'POST':
        print(request.POST)
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        # user.is_staff = request.POST.get('is_staff')
        # user.is_active = request.POST.get('is_active')
        user.save()
    return render(request, 'accounts/profiledetailview.html', {'form':form})



from django.views import View
from .forms2 import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
class UserRegistrationView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/userregistration.html', {'form':form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            return HttpResponseRedirect("accounts/profileview/1/")
        else:
            return render(request, 'accounts/userregistration.html', {'form':form})
    