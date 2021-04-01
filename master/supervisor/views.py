
from django.shortcuts import render
from supervisor.mixins import CartMixin
from django.views.generic import View
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import Supervisor


def index(request):
    return render(request, 'supervisor/index.html')


class LoginView(CartMixin, View):

    def get (self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        #categories = Category.objects.all()
        context = {'form': form}
        return render(request, 'supervisor/login.html', context)

    def post (self, request, *args, **kwargs):

        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')

        return render(request, 'supervisor/login.html', {'form': form})


class RegistrationView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        return render(request, 'supervisor/registration.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            b = Supervisor(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                first_name =form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
            )

            b.save()

            user = authenticate(username=form.cleaned_data['username'], password = form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'supervisor/registration.html', context)


class ProfileView(CartMixin, View):

    def get(self, request,  *args, **kwargs):
        supervisor = Supervisor(user=request.user)
        return render(request, 'supervisor/profile.html', {'supervisor': supervisor} )