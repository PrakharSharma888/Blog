from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registered for {username}')
            redirect('postt')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form':form})

@login_required
def profile(request):

    if request.method == 'POST':
        if request.POST.get('update_button') == 'updatepro':
            update_form = UserUpdateForm(request.POST, instance=request.user)
            update_profile = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if update_form.is_valid() and update_profile.is_valid():
                update_form.save()
                update_profile.save()
                messages.success(request,'You have updated your profile!')
                redirect('profile')
            else:
                update_form = UserUpdateForm(instance=request.user)
                update_profile = ProfileUpdateForm(instance=request.user.profile)

            context = {
                'update_form': update_form,
                'update_p_form': update_profile,
                'update': True
            }
            return render(request, 'users/profile.html', context)
        else:
            print("done")
            update_form = UserUpdateForm(request.POST, instance=request.user)
            update_profile = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if update_form.is_valid() and update_profile.is_valid():
                update_form.save()
                update_profile.save()
                messages.success(request, 'You have updated your profile!')
                redirect('profile')
            else:
                update_form = UserUpdateForm(instance=request.user)
                update_profile = ProfileUpdateForm(instance=request.user.profile)

            context = {
                'update_form': update_form,
                'update_p_form': update_profile,
                'update': True
            }
            return render(request, 'users/profile.html', context)
    return render(request,'users/profile.html')


def favicon(request):
    pass