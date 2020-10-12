from django.shortcuts import render, reverse, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import DetailView, CreateView, UpdateView

from users.forms import CreateUserForm



def registration(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, 'Użytkownik ' + user + ' został zrejestrowany.' )
            return redirect("Login")

    return render(request, "registration.html", {"form": form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_page')
        else:
            messages.info(request, "Invalid username or password.")

    context = {}
    return render(request, "login.html", context={})


def user_logout(request):
    logout(request)
    return redirect("Home_page")





# class EditAccount(UpdateView):
#     model = Users
#     form_class = EditForm
#     template_name = "edit_account.html"

#     @property
#     def success_url(self):
#         return reverse('My_account', kwargs={'username': self.request.user})


# def change_password(request):
#     if request.method == 'POST':
#         form = PassForm(request.POST)
#         if form.is_valid():
#             password = form.cleaned_data.get('password')
#             user = request.user
#             user.set_password(password)
#             user.save()
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('Login')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PassForm()
#     return render(request, 'change_password.html', {'form': form})
