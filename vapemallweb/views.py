
from django.shortcuts import render, get_object_or_404, redirect
#from .models import Client
#ClientView function
def clientView(request):
    #clients = Client.objects.all().order_by('first_name')
    return render(request, 'client.html')
# Create your views here.
