"""oop_grp_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from app import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^admin/', admin.site.urls),
    url(r'^approve_rec/$', views.approve_rec, name='approve_rec'),
    url(r'^approve_rec/approve/(?P<id>\d+)/$', views.approve, name='approve'),
    url(r'^approve_doc/$', views.approve_doc, name='approve_doc'),
    url(r'^approve_doc/approved/(?P<id>\d+)/$', views.approved, name='approved'),
    url(r'^req_doc/$', views.req_doc, name='req_doc'),
    url(r'^req_doc/approvedoc/(?P<id>\d+)/$', views.approvedoc, name='approvedoc'),
    url(r'^doctordb/$', views.req_rec, name='doctordb'),
    url(r'^doctordb/approvedoc/(?P<id>\d+)/$', views.approvedoc, name='approvedoc'),
    url(r'^doctordb/approve/(?P<id>\d+)/$', views.approve, name='approve'),
    url(r'^patientdb/$', views.patientdb, name='patientdb'),
    url(r'^patientdb/approve_doc/(?P<id>\d+)/$', views.approve_doc, name='approvedoc'),
    url(r'^patientdb/approved/(?P<id>\d+)/$', views.approved, name='approved'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
