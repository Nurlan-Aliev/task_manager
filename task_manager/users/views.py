from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from task_manager.users.forms import UsersForm


class Users(View):

    def get(self, request):
        users = User.objects.all()
        context = {'users': users}
        return render(request, 'users/users.html', context)


class CreateUser(View):

    def get(self, request, *args, **kwargs):
        form = UsersForm()
        return render(request, 'users/create_user.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        messages.add_message(request, messages.ERROR, 'Некорректная Форма')
        return redirect(reverse('create_user'))



class UpdateUser(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


# class DeleteUser(View):
#
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass
#