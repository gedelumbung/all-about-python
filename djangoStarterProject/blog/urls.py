from django.conf.urls import url

from . import blog

urlpatterns = [
    url(r'^$', blog.index, name='index'),
    url(r'^about/$', blog.about, name='about'),
]