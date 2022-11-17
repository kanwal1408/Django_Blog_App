from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)  #for grabbing the data from the user
        if form.is_valid(): # checks whether data entered in all the fields is according to class specified in the models.py
            form.save()
            return redirect('users-login')
    else:
        form = SignUpForm()
    context ={
        'form' : form,
    }
    return render(request, 'users/sign_up.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid(): # for saving the changed information in edit profile modal
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user) #because of instance , username is seen by default when edit profile modal opens
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context ={
        'u_form' : u_form,
        'p_form' : p_form,
    }

    return render(request, 'users/profile.html',context)