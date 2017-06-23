# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):

    error_messages = request.session['context']
    return render(request, 'Login_Registration_app/index.html', error_messages)

def register(request):
    context = {}
    new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
    print new_user

    try:
        new_user.full_clean()
    except ValidationError as error:
        for key in error:
            context[key[0]] = key[1][0]
    print context

    if request.POST['password'] != request.POST['password_confirm']:
        context['pw_mismatch'] = 'Passords do not match'
        
    if context == {}:
        print ('******************')
        new_user.save()
        context['result'] = 'Registration Complete!'
        request.session['context'] = context
        return redirect('/success')

    else:

        context['result'] = 'Reigstration failed. Please try again.'
        request.session['context'] = context
        return redirect('/')

def success(request):


    return render(request, 'Login_Registration_app/success.html')
