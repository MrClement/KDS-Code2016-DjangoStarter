from django.conf.urls import url

from . import views

# This is you router. Whenever someone uses their brower to visit your app
# this bit of code decides what page to show them based on the url that
# they request

# A few hints:
# - ^ means the start of a string, and $ means the end
# - <value> means pass that value to the view so it knows which ToDo was referenced

urlpatterns = [
    # this says that any url that has no additonal characters in it (it starts, then ends)
    # is sent to the index view. Because firstapp is just one app on your server this
    # means that the url to access this page is http://localhost:8000/firstapp
    url(r'^$', views.index, name='index'),
    # Here we match any number (at least one digit, 0-9) and call that the todo_id
    url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
    #handle new todo
    url(r'^new/$', views.new, name='new'),
]
