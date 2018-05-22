from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/show/(?P<id>\d+)$', views.show),
    # When you want to show a special input which is connected with the database
    url(r'^users/edit/(?P<id>\d+)$', views.edit),
    url(r'^users/update/(?P<id>\d+)$',views.update),
    url(r'^users/destroy/(?P<id>\d+)$',views.destroy)
]

# users/create send the user to the logic method in this example (create)
# users/new send the user to the method which shows the html file

# The users/show redirects the user to the show index file

# The users/update route is connected with the update function which redirects to the index file

# users/edit just display the user the edit html file