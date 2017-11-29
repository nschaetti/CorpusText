
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name="home"),                    # Corpus home
    url(r'^texts/(?P<id_text>\d+)$', views.view_text),          # View text
    url(r'^texts/list/(?P<year>\d{4})$', views.list_texts),     # View text for a year
    url(r'^date$', views.current_time, name="date"),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition, name="addition")
]

