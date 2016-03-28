from django.shortcuts import render
from django.contrib import messages
from boats_auth import utils as auth_utils
from logic import forms
from logic import utils as logic_utils


def estimate_view(request):

    auth_utils.register_ip_address(request)

    est_price_euro = None

    if request.POST:

        form = forms.EstimateBoatForm(request.POST)

        if form.is_valid():

            est_price_euro = logic_utils.estimate_asking_price_euro(
                form)

            messages.info(
                request,
                'Boat estimated at {:.0f} euro'.format(
                    est_price_euro))

        else:
            messages.info(request, 'Invalid input.')

    else:
        form = forms.EstimateBoatForm()

    context = {'form': form,
               'est_price_euro': est_price_euro,
               'current_view': 'estimate_view'}

    return render(request, 'logic/estimate.html', context)


def plots_view(request):

    context = {'current_view': 'plots_view'}
    return render(request, 'logic/plots.html', context)
