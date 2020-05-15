from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .forms import RegisterForm, EditAccountForm
# Create your views here.

@login_required
def dashboard(request):
    template_name = 'registration/dashboard.html'
    return render(request, template_name)

def register(request):
    template_name = 'registration/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    messages.info(request, "Sessão Encerrada!")
    return redirect("core:home")

@login_required
def edit(request):
    template_name = 'registration/edit.html'
    context = {}
    form = EditAccountForm()
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    
    return render(request, template_name, context)

@login_required
def edit_senha(request):
    template_name = 'registration/edit_senha.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['sucsess'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
