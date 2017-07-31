from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from primeForm import views

urlpatterns = [
	url(r'^homepage/$', views.homepage, name='homepage'),
	url(r'^primeformfinder/$', views.primeformfinder, name='primeformfinder'),
	url(r'^transpose/$', views.transpose, name='transpose'),
	url(r'^invert/$', views.invert, name='invert'),
	url(r'^retrograde/$', views.retrograde, name='retrograde'),
	url(r'^intervalsfinder/$', views.intervalsfinder, name='intervalsfinder'),
]

