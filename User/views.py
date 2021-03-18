from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



class CreateUserView(SuccessMessageMixin,generic.CreateView):
    model = User
    form_class = UserRegisterForm
    # success_message = f"New user of name {cleaned_data.get('username')}"
    # def form_valid(self, form):
    #     user = form.cleaned_data.get('username')
    #     success_message = f"New user has been sucessfully created of username {user}"
    #     return super().form_valid(form)
    template_name='create_user.html'
    success_url = 'login'

def UpdateUserView(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your profile has been sucessfully updated")
            return redirect('update_user')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'user_profile.html', context)    

# user login view





    



