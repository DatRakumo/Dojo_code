from django.conf.urls import url
from django.views.generic import TemplateView

from views import HomeView
from my_app.views import Home
from demo.views import Demo


urlpatterns = [
    url(r'hi', Home.as_view(template_name='index.html')),
    url(r'hello', HomeView.as_view(template_name='home.html')),
    url(r'demo', Demo.as_view(template_name='demo.html')),
]