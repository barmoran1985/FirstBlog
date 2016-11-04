from django.conf.urls import url
import views
from django.views.static import serve

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_details)
]
