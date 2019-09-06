from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
from django.urls import path, include
from django.utils.translation import ugettext_lazy as _
from sismedclin import views

from material.admin.sites import site

site.site_header = _('SISMEDCLIN')
site.site_title = _('SisMedClin - Sistema web para Clinicas e Consultorios')
site.favicon = staticfiles('path/to/favicon')

urlpatterns = [
    
    path(r'', views.home),
    path('admin/', include('material.admin.urls')),
    path('admin/', admin.site.urls),
]
