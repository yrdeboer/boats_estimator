from django.conf.urls import url

from logic import views

urlpatterns = [
    url(r'^estimate$', views.estimate_view, name='estimate_view'),
    url(r'^plots$', views.plots_view, name='plots_view'),
]
