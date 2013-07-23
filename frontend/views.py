# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
import datetime

@login_required
def index_view(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {"foo": "bar"})

def logout_view(request):
	logout(request)
	return redirect('/')
