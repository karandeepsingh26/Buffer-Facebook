from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import render
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialLogin
from allauth.socialaccount.models import SocialAccount

from django.db import models
from django.contrib.auth.models import User


import facebook
from status.forms import StatusForm
from models import User

import facebook
# from statys.models import UserProfile

def index(request):
	# user = request.user
	form=StatusForm(request.POST or None)
	# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

	instance = None
	token = None
	if request.user.is_authenticated:
		context = RequestContext(request,
			{'request': request,
			'user': request.user,

			'form':form})
		if request.user.is_anonymous() is not True:
			# instance = User.objects.filter(first_name__contains='jeevan')
			# instance = SocialAccount.objects.filter(user__first_name__contains='jeevan')
			instance = SocialToken.objects.filter(account__user__first_name__contains='parvez')

			for e in instance:
				token = e
				print token
		#print instance.SocialToken
	if request.method=="POST":
			if request.user.is_authenticated:
				graph = facebook.GraphAPI(token)
				data=request.POST.get('text')
				graph.put_object('me', 'feed', message=data)
				return render(request,"home.html",context)

	return render(request,"home.html",context)