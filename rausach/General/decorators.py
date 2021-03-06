from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, decorators

def is_admin(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        # print(user.username)
        if user.role == 0:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('General:login'))
    return wrapper