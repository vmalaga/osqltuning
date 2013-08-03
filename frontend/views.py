from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from models import DbConnections
from models import DbConnectionsForm

import cx_Oracle

@login_required
def index_view(request):
  qs = DbConnections.objects.all()
  return render(request, 'index.html', {"connlist": qs})

def logout_view(request):
  logout(request)
  return redirect('/')

def test_view(request):
  qs = DbConnections.objects.values()
  return render_to_response('textview.html',{'connlist': qs})

def dbconnform(request):
	if request.method == 'POST':
		form = DbConnectionsForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = DbConnectionsForm()

	return render(request, 'dbcon.html', {'form': form})

def dbconn(conname):
  conname = conname
  
def conn_actions(request):
  hostname = request.POST['hostname']
  username = request.POST['username']
  password = request.POST['password']
  service = request.POST['servicename']
  dsn_tns = cx_Oracle.makedsn(hostname, 1521, service)
  if request.POST['action'] == 'Test':
    message = 'TEST: ' + 'Hostname: ' + hostname + ' username: ' + username + ' password: ' + password + ' service: ' + service
    if username == 'sys':
      db = cx_Oracle.connect(username, password, dsn_tns, mode = cx_Oracle.SYSDBA)
      print db.version
    else:
      db = cx_Oracle.connect(username, password, dsn_tns)
      print db.version
  else:
    message = 'SAVE: ' + 'Hostname: ' + hostname + ' username: ' + username + ' password: ' + password + ' service: ' + service
    name = username + '@' + service
    try:
      n = DbConnections(conname=name,hostname=hostname,username=username,password=password,servicename=service)
      n.save()
      message = message + ' OK SAVED ...'
      return HttpResponseRedirect('/')
    except:
      pass
  return HttpResponse(message)
