from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from account.models import Account
from django.db.models import F, Sum
from django.utils.translation import gettext as _

from .decorator import unauthenticated_user, allowed_users
from datetime import datetime, time, timedelta
from django.utils import translation    
import re
from django.db.models import Q
import operator 

from . import forms
import csv

from .forms import NewUserForm


from django.contrib.auth.models import Group

import json
import sweetify

from django.shortcuts import render
from django.template import RequestContext

import hashlib
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from uuid import uuid4

from random import randint
import sys
import logging
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib.sessions.models import Session

from .models import History
from .models import LuckyNumber
from .models import LuckyNumberOrders
from .models import WinningNumber
from .models import Product
from .models import Redeem

from .models import TopUp
from .models import Convert

import random

def create_transaction(category, wallet, amount, member, associate, mode):
    #Create TransactionList
    transaction_category = {'category': category}
    transaction_wallet = {'wallet': wallet}
    transaction_amount = {'amount': amount}
    transaction_member = {'member': member}
    transaction_receipient = {'associate': associate}
    transaction_mode = {'mode': mode}
    transaction_final = {**transaction_category, **transaction_wallet, **transaction_amount, **transaction_member, **transaction_mode}
    History.objects.create(**transaction_final)
    
def generateUUID():
    return str(uuid4().hex)

    

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

@login_required(login_url="/signin")
def dashboard(request):
    return render(request=request,
                  template_name="dashboard/dashboard.html",
                  context={
                  })

@login_required(login_url="/signin")
def maintenance(request):
    sweetify.info(request, 'Coming Soon', text='Be Excited', persistent='Close')
    return redirect("/dashboard")
    return render(request=request,
                  template_name="dashboard/dashboard.html",
                  context={
                  })

@login_required(login_url="/signin")
def lucky_number(request):
    formF = forms.FrontLuckyNumber()
    formB = forms.BackLuckyNumber()
    if request.method == 'POST' and 'frontSequence' in request.POST:
        formF = forms.FrontLuckyNumber(request.POST)
        if formF.is_valid():
            member = Account.objects.get(username=request.user)
            quantity = formF.cleaned_data.get('quantity')
            string1 = str(formF.cleaned_data.get('num1'))
            string2 = str(formF.cleaned_data.get('num2'))
            string3 = str(formF.cleaned_data.get('num3'))
            string4 = str(formF.cleaned_data.get('num4'))
            frontS = (string1 + string2 + string3 + string4)
            print(frontS)

            if member.gold >= (quantity * 1):

                savedID = generateUUID()
                print(savedID)
                order_member = {'member': member}
                order_id = {'order_id': savedID}
                order_amount = {'amount': quantity * 1}
                order_final = {**order_id, **order_member, **order_amount}
                LuckyNumberOrders.objects.create(**order_final)

                for x in range(quantity):
                    randomizeS = str(random.randint(0, 999))
                    randomizedFinal = randomizeS.zfill(3)
                    ticket = frontS + randomizedFinal
                    print(ticket)
                    print(savedID)
                    ticket_member = {'member': member}
                    ticket_number = {'number': ticket}
                    ticket_amount = {'amount': 1}
                    ticket_order = {'order': LuckyNumberOrders.objects.get(order_id=savedID)}
                    ticket_final = {**ticket_member, **ticket_number, **ticket_amount, **ticket_order}
                    LuckyNumber.objects.create(**ticket_final)
                    
                create_transaction('LUCKY', 'Gold', quantity, member, '', 'OUT')

                sweetify.success(request, 'Success', text='Successfully bought ' + str(quantity) + " ticket", persistent='Close')
                return redirect("/lucky_number")
            else:
                sweetify.warning(request, 'Insufficient Balance', text='Insufficient amount of Gold Coins to Participate', persistent='Close')
                return redirect("/lucky_number")

    elif request.method == 'POST' and 'backSequence' in request.POST:
        formB = forms.BackLuckyNumber(request.POST)
        if formB.is_valid():
            print(formB.cleaned_data.get('num1'))
            sweetify.warning(request, 'Error', text='Username has been used', persistent='Close')
    return render(request=request,
                  template_name="dashboard/luckynumber.html",
                  context={
                      "formF":formF,
                      "formB":formB,
                      "tickets": LuckyNumberOrders.objects.filter(member=request.user).all(),
                  })

def lucky_number_details(request, ticket_id):
    order_obj = LuckyNumberOrders.objects.get(order_id=ticket_id)
    tickets = order_obj.ticket.all()
    return render(request = request,
                    template_name = "dashboard/lucky_number_details.html",
                    context={
                        "order":order_obj,
                        "tickets":tickets
                    })

@login_required(login_url="/signin")
def affliate(request):
    parent_node = Account.objects.get(username=request.user)
    # total_tree = parent_node.get_descendants(include_self=True)
    total_tree = (parent_node.get_descendants(include_self=True)
                .annotate(relative_level=F('level') - parent_node.level))
    return render(request=request,
                  template_name="dashboard/affliate.html",
                  context={
                      "accounts": total_tree,
                  })

@login_required(login_url="/signin")
def register_member(request):
    form = forms.MemberUserForm()
    formAmount = forms.Point()
    if request.method == "POST":
        form = forms.MemberUserForm(request.POST)
        formAmount = forms.Point(request.POST)
        print("Test")
        if form.is_valid() and formAmount.is_valid():
            print("Test2")
            print(form.cleaned_data.get('password1'))
            print(form.cleaned_data.get('password2'))
            point = int(formAmount.cleaned_data.get('amount'))
            current_user = Account.objects.get(username=request.user)
            if current_user.ruby >= int(point):
                current_user.ruby = current_user.ruby - point
                current_user.save()

                instance = form.save(commit=False)
                instance.parent = request.user
                instance.raw_password = form.cleaned_data.get('password1')
                instance.gold = instance.gold + point
                instance.save()

                create_transaction('REGISTRATION', 'Ruby', int(point), current_user, '', 'OUT')

                create_transaction('REGISTRATION', 'Gold', int(point), Account.objects.get(username=instance.username), '', 'IN')

                reward = 0

                if (current_user.children.count()) == 2:
                    print("Reward 30")
                    reward = 30
                elif (current_user.children.count()) == 6:
                    print("Reward 60")
                    reward = 60
                elif (current_user.children.count()) == 15:
                    print("Reward 120")
                    reward = 120
                elif (current_user.children.count()) == 31:
                    print("Reward 240")
                    reward = 240
                elif (current_user.children.count()) == 48:
                    print("Reward 480")
                    reward = 480

                create_transaction('COMMISSION', 'Gold', reward, current_user, '', 'IN')

                current_user.gold = float(current_user.gold) + float(reward)
                current_user.save()

                

                username = form.cleaned_data.get('username')
                sweetify.success(request, 'Success', text='Account has been registered', persistent='Close')
                return redirect("main:register_member")
        else:
            username_check = (form.cleaned_data.get('username'))
            try:
                username = Account.objects.get(username=username_check)
            except Account.DoesNotExist:
                username = None

            if username is not None or username != "":
                sweetify.warning(request, 'Error', text='Username has been used', persistent='Close')
            if form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
                sweetify.warning(request, 'Error', text='Password doesnt match', persistent='Close')

    form = forms.MemberUserForm()

    return render(request=request,
                  template_name="dashboard/register-member.html",
                  context={
                      "form":form,
                      "formAmount":formAmount,
                  })

@login_required(login_url="/signin")                 
def history(request):
    return render(request=request,
                  template_name="dashboard/history.html",
                  context={
                      "histories":History.objects.filter(member=request.user).all()
                  })

@login_required(login_url="/signin")
def topup(request):
    form = forms.TopUp()
    if request.method == "POST":
        form = forms.TopUp(request.POST)
        if form.is_valid():
            topup_member = {'member': request.user}
            topup_amount = {'amount': form.cleaned_data.get('amount')}
            topup_final = {**topup_member, **topup_amount}
            TopUp.objects.create(**topup_final)


            sweetify.success(request, 'Top Up Requested', text='Your top up has been requested, please follow the instruction for payment', persistent='Close')
            return redirect("main:topup")

    return render(request=request,
                  template_name="dashboard/topup.html",
                  context={
                      "form":form,
                      "topups":TopUp.objects.filter(member=request.user).all()
                  })

@login_required(login_url="/signin")
def convert(request):
    form = forms.Convert()
    if request.method == "POST":
        form = forms.Convert(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            current_user = Account.objects.get(username=request.user)
            if float(current_user.ruby) >= float(amount):
                convert_member = {'member': request.user}
                convert_amount = {'amount': amount}
                convert_final = {**convert_member, **convert_amount}
                Convert.objects.create(**convert_final)

                current_user.ruby = float(current_user.ruby) - float(amount)
                current_user.gold = float(current_user.gold) + float(amount)
                current_user.save()

                create_transaction('CONVERT', 'Ruby', float(amount), current_user, '', 'OUT')
                create_transaction('CONVERT', 'Gold', float(amount), current_user, '', 'IN')
                
                sweetify.success(request, 'Success', text='Conversion completed', persistent='Close')
                return redirect("main:convert")
            else:
                sweetify.warning(request, 'Insufficient Ruby', text='Insufficient for conversion', persistent='Close')
                return redirect("main:convert")
    return render(request=request,
                  template_name="dashboard/convert.html",
                  context={
                      "form":form,
                      "converts":Convert.objects.filter(member=request.user).all()
                  })


@login_required(login_url="/signin")
def edit_profile(request):
    return render(request=request,
                  template_name="dashboard/edit-profile.html",
                  context={
                  })

def homepage(request):
    return render(request=request,
                  template_name="main/homepage.html",
                  context={
                  })


def ticket(request):
    return render(request=request,
                  template_name="main/ticket.html",
                  context={
                  })

def signup(request):
    form = forms.NewUserForm()
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)
        print("Test")
        if form.is_valid():
            print("Test2")
            print(form.cleaned_data.get('password1'))
            print(form.cleaned_data.get('password2'))
            instance = form.save(commit=False)
            instance.raw_password = form.cleaned_data.get('password1')
            instance.save()
            # group = Group.objects.get(name='group_name')
            # instance.groups.add(group)
            username = form.cleaned_data.get('username')
            sweetify.success(request, 'Success', text='Account has been registered', persistent='Close')
            return redirect("/")
        else:
            username_check = (form.cleaned_data.get('username'))
            try:
                username = Account.objects.get(username=username_check)
            except Account.DoesNotExist:
                username = None

            if username is not None or username != "":
                sweetify.warning(request, 'Error', text='Username has been used', persistent='Close')
            if form.cleaned_data.get('password1') != form.cleaned_data.get('password2'):
                    sweetify.warning(request, 'Error', text='Password doesnt match', persistent='Close')

    form = forms.NewUserForm()
    return render(request = request,
                  template_name = "main/signup.html",
                  context={"form":form})

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in")
                return redirect("/dashboard")
            else:
                sweetify.error(request, 'Error', text='Wrong Username or Password', persistent='Close')
        else:
            sweetify.error(request, 'Error', text='Wrong Username/Password or Verfication', persistent='Close')
    form = AuthenticationForm()
    return render(request,
                  "dashboard/login.html",
                  {"form":form})

@login_required(login_url="/signin")
def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out Successfully")
    return redirect("main:dashboard")

