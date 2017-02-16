from django.conf.urls import url
import views

app_name = 'call_detail'
urlpatterns = [
    url('^index/$', views.index_view, name='index'),
    
]
