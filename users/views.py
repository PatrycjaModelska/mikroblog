from django.shortcuts import render, reverse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView, UpdateView

from users.models import Users
from users.forms import RegisterForm, UserForm, EditForm, PassForm


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form})


def user_logout(request):
    logout(request)
    return redirect("Home_page")


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
        else:
            return render(request, "registration.html", {"form": form, "errors": form.errors})
    else:
        form = RegisterForm()
    return render(request, "registration.html", {"form": form})


class MyAccount(CreateView):
    model = Users
    form_class = UserForm
    template_name = "my_account.html"


class EditAccount(UpdateView):
    model = Users
    form_class = EditForm
    template_name = "edit_account.html"

    @property
    def success_url(self):
        return reverse('My_account', kwargs={'username': self.request.user})


def change_password(request):
    if request.method == 'POST':
        form = PassForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = request.user
            user.set_password(password)
            user.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('Login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PassForm()
    return render(request, 'change_password.html', {'form': form})
