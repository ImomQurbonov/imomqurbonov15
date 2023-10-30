from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import (
    get_user_model,
    login, logout, authenticate,
    hashers
)
from django.contrib import messages

User = get_user_model()

class LoginView(View):
    template_name = 'login.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Username or password is not valid !')
            return render('/login')


class SignupView(View):
    template_name = 'signup.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists !!!')
                return redirect('/signup')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists !!!')
                return redirect('/signup')
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=hashers.make_password(password2)
            )
            user.save()
            return redirect('/login')
        else:
            messages.error(request, 'Passwords are not same')
            return redirect('/signup')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/home')

