from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import User

def user_create(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		"form":form,
	}	
	return render(request,"messaging/add_user.html",context)
