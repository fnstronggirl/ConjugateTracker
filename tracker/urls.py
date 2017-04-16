from django.conf.urls import url

from . import views
app_name = "tracker"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^squat_movement/(?P<pk>[0-9]+)/$', views.SquatDetailView.as_view(), name='squat_detail'),
    url(r'^deadlift_movement/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='deadlift_detail'),
    url(r'^bench_movement/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='bench_detail'),
    url(r'^lower_movement/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='lower_detail'),
    url(r'^upper_movement/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='upper_detail'),
    url(r'^squat_movement/new$', views.new_squat, name='squat_new'),
    url(r'^deadlift_movement/new$', views.new_deadlift, name='deadlift_new'),
    url(r'^bench_movement/new$', views.new_bench, name='bench_new'),
    url(r'^lower_movement/new$', views.new_lower, name='lower_new'),
    url(r'^upper_movement/new$', views.new_upper, name='upper_new'),
]