from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

# SIGNUP code
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# LOGIN code
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add_weight')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# LOGOUT code
@login_required(login_url='/login/')
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    context = {
        'user': request.user
    }

    return render(request, 'logout.html', {'user': context})
