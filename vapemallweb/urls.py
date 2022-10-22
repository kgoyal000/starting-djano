from django.urls import path
from . import views
app_name = 'vapemallweb'
urlpatterns = [
    path('', views.clientView, name='client_view'),
]
