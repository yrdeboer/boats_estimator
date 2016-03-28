from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from boats_auth import utils


def login_view(request):

    (next_view, next_url) = utils.get_next_view_and_url(request)

    if request.POST:

        form = AuthenticationForm()

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:

            login(request, user)

            return HttpResponseRedirect(reverse(next_view))

        else:

            messages.error(request, 'Invalid credentials.')

    else:

        form = AuthenticationForm()

    context = {'form': form,
               'next_url': next_url,
               'current_view': 'login_view'}

    return render(request, 'boats_auth/login.html', context)

            
def logout_view(request):

    logout(request)
    
    # messages.error(request, 'User logged out.')

    return HttpResponseRedirect(reverse('boats_auth:login_view'))

