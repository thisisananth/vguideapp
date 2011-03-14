# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.shortcuts import render_to_response
from mits.forms import DecideForm
from mits.forms import TrackForm
from mits.forms import LoginForm
from mits.models import Task
from django.core.context_processors import csrf
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import list_detail
from django.contrib.auth.models import User
from django.views.generic.simple import direct_to_template

from mits.forms import UserCreationFormExtended

def viewmit(request):
    return HttpResponse("Hello world")




def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
@login_required
def decide(request):
        c = {}
        c.update(csrf(request))
	id = request.session['_auth_user_id']
	user = User.objects.get(pk=id)
        if request.method == 'POST':
            form = DecideForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
		
		p1 = Task(pub_date=datetime.date.today(),user=user,task1=str(cd['task1']),schd_poms1=cd['poms1'],used_poms1=0,completed1=False,task2=str(cd['task2']),
			  schd_poms2=cd['poms2'],used_poms2=0,completed2=False,task3=str(cd['task3']),schd_poms3=cd['poms3'],used_poms3=0,completed3=False)
		p1.save()
		return HttpResponseRedirect('/track/')
            else:
                c.update({'form': form})
                return render_to_response('decide_form.html', c)
                
            
           
        else:
	    try:
		task = Task.objects.get(pub_date=datetime.date.today(),user=user)
		return track(request)
	    except ObjectDoesNotExist:
		form = DecideForm()
		c.update({'form': form})
		return render_to_response('decide_form.html', c)
		
		
            
	
	

@login_required
def track(request):
    
    c = {}
    c.update(csrf(request))
    id = request.session['_auth_user_id']
    user = User.objects.get(pk=id)
    try:
	task = Task.objects.get(pub_date=datetime.date.today(), user=user)
    except ObjectDoesNotExist:
	task=None
	
    
    if request.method == 'POST':
	task1 = Task.objects.get(pub_date=datetime.date.today(),user=user)
	form = TrackForm(request.POST,instance = task1)
	if form.is_valid():
	    cd = form.cleaned_data
	    if not task.completed1:
		task1.completed1 = cd ['completed1']
		task1.used_poms1 = cd ['used_poms1']
	    else:
		task1.completed1 = task.completed1
		task1.used_poms1 = task.used_poms1
	    if not task.completed2:
		task1.completed2 = cd ['completed2']
		task1.used_poms2 = cd ['used_poms2']
	    else:
		task1.completed2 = task.completed2
		task1.used_poms2 = task.used_poms2
	    if not task.completed3:
		task1.completed3 = cd ['completed3']
		task1.used_poms3 = cd ['used_poms3']
	    else:
		task1.completed3 = task.completed3
		task1.used_poms3 = task.used_poms3
	    task1.save()
	    return HttpResponseRedirect('/track/')
	else:
                c.update({'form': form})
		
		taskList=Task.objects.filter(pub_date=datetime.date.today(),user=user)
		c.update({'task':taskList[0]})
		c.update({'username':user.username})
                return render_to_response('task_view.html', c)
    else:
	if task == None:
	    return decide(request)
	else:
	    c = {'task':task}
	    c.update({'form':TrackForm(instance=task)})
	    c.update(csrf(request))
	    c.update({'username':user.username})
	    
	    
	    return render_to_response('task_view.html',c)
    

def register(request):
    c = {}
    c.update(csrf(request))
    
    if request.method == 'POST':
        form = UserCreationFormExtended(request.POST)
        if form.is_valid():
            new_user = form.save()
	    c.update({'fromregister': True})
	    c.update({'form':LoginForm()})
	    return render_to_response('login.html',c)
	else:
	    c.update({'form': form})
            return render_to_response('register.html', c)
	
    else:
        form = UserCreationFormExtended()
	c.update({'form':form})
    return render_to_response("register.html", c)

def login(request):
    c = {}
    c.update(csrf(request))
    
    if request.method == 'POST':
	form = LoginForm(request.POST)
	if form.is_valid():
	    cd = form.cleaned_data
	    username = cd['username']
	    password = cd['password']
	    user = auth.authenticate(username=username, password=password)
	    if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect("/decide/")
	    else:
		c.update({'form':form})
		c.update({'error':True})
		return render_to_response('login.html',c)
	else:
	    c.update({'form':LoginForm()})
	    return render_to_response('login.html',c)
		
    else:
        c.update({'form':LoginForm()})
        return render_to_response('login.html',c)

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/login/")
    

@login_required
def celebrate(request):
    user = User.objects.get(pk=request.session['_auth_user_id'])
    return list_detail.object_list(request,
		      queryset=Task.objects.all().filter(user =user )[0:7],
		      template_name = 'celebrate_view.html')
    
@login_required  
def hidden_contact(*args,**kwargs):
    return direct_to_template(*args,**kwargs)
