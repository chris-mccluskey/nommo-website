from django.shortcuts import render
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View, RedirectView
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Country, Category, Investment
from .forms import SignUpForm
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from django.db.models import F

def is_staff(user):
    return user.is_staff


def get_rank(obj):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {'X-CMC_PRO_API_KEY': 'd7b02d27-ae3e-414d-b8bb-aaaffa7049ea'}
    response = requests.get(url, headers=headers)
    for coin in response.json()['data']:
        if coin['slug'] == obj.name.lower():
            return int(coin['cmc_rank'])


class HomeView(TemplateView):
    template_name = 'index.html'


class InvestmentsView(TemplateView):
    template_name = 'investments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        investments = Investment.objects.all()
        print(self.request.GET)


        if 'q' in self.request.GET:
            q = self.request.GET['q']
            investments = investments.filter(name__icontains=q)

        for inv in investments:
            print(inv)
            rank = get_rank(inv)
            inv.rank = int(rank)
            print(inv.rank)

        context['investments'] = investments

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)


        request.session.setdefault('favorite_investments', [])
        request.session.save()

        return self.render_to_response(context)


class InvestmentView(DetailView):
    model = Investment
    template_name = 'investment.html'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_staff), name='dispatch')
class CreateInvestmentView(CreateView):
    model = Investment
    fields = ['name', 'description', 'category']
    template_name = 'create_investment.html'
    success_url = '/investments'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_staff), name='dispatch')
class EditInvestmentView(UpdateView):
    model = Investment
    fields = ['name', 'description', 'category']
    template_name = 'edit_investment.html'
    success_url = '/investments'


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_staff), name='dispatch')
class DeleteInvestmentView(DeleteView):
    model = Investment
    success_url = '/investments'


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup_form'] = SignUpForm()
        return context

    def post(self, request, *args, **kwargs):
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = User.objects.create(username=request.POST['username'])
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect('index')
        return render(request, 'signup.html', context={'signup_form': signup_form})


class AuctionView(TemplateView):
    template_name = 'auction.html'
