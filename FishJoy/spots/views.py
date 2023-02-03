from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import DataMixin


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page was not found</h1>")


def about(request):
    mixin = DataMixin()
    context = mixin.get_user_context(title='About')
    return render(request, 'spots/about.html', context)


class FisherHome(DataMixin, ListView):
    model = Spots
    template_name = 'spots/home.html'
    context_object_name = 'spots'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Home page')
        return {**context, **c_def}

    def get_queryset(self):
        return Spots.objects.order_by('-rating').select_related('spot_category')


class ShowFish(DataMixin, ListView):
    model = Fish
    template_name = 'spots/show_fish.html'
    context_object_name = 'fish'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Fish')
        return {**context, **c_def}

    # def get_queryset(self):
    #     return Spots.objects.filter(fish__slug=self.kwargs['single_fish_slug'])


class ShowBaits(DataMixin, ListView):
    model = Baits
    template_name = 'spots/show_baits.html'
    context_object_name = 'baits'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Baits')
        return {**context, **c_def}


class ShowSpot(DataMixin, DetailView):
    model = Spots
    template_name = 'spots/show_spot.html'
    context_object_name = 'spot'
    slug_url_kwarg = 'spot_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Spot - ' + str(context['spot'].title))
        return {**context, **c_def}


class ShowSingleFish(DataMixin, DetailView):
    model = Fish
    template_name = 'spots/show_single_fish.html'
    context_object_name = 'fish'
    slug_url_kwarg = 'single_fish_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Fish - ' + str(context['fish'].name))
        return {**context, **c_def}


class ShowSpotsCategory(DataMixin, ListView):
    model = Spots
    template_name = 'spots/home.html'
    context_object_name = 'spots'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Spot category - ' + str(context['spots'][0].spot_category))
        return {**context, **c_def}

    def get_queryset(self):
        return Spots.objects.filter(spot_category__slug=self.kwargs['spots_category_slug']).order_by('-rating').\
            select_related('spot_category')


class ShowFishCategory(DataMixin, ListView):
    model = Fish
    template_name = 'spots/show_fish.html'
    context_object_name = 'fish'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Fish category - ' + str(context['fish'][0].fish_category))
        return {**context, **c_def}

    def get_queryset(self):
        return Fish.objects.filter(fish_category__slug=self.kwargs['fish_category_slug']).select_related(
            'fish_category')


class AddSpot(DataMixin, CreateView):
    form_class = AddSpotForm
    template_name = 'spots/add_form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add spot')
        return {**context, **c_def}


class AddFish(DataMixin, CreateView):
    form_class = AddFishForm
    template_name = 'spots/add_form.html'
    success_url = reverse_lazy('fish')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add fish')
        return {**context, **c_def}


class AddBait(DataMixin, CreateView):
    form_class = AddBaitForm
    template_name = 'spots/add_form.html'
    success_url = reverse_lazy('baits')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add bait')
        return {**context, **c_def}


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'spots/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        return {**context, **c_def}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'spots/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Login')
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def search(request):
    mixin = DataMixin()
    context = mixin.get_user_context(title='Search')
    searched = request.POST['searched']

    spots_data = Spots.objects.filter(title__icontains=searched) | \
                 Spots.objects.filter(rating__icontains=searched) | \
                 Spots.objects.filter(location__icontains=searched) | \
                 Spots.objects.filter(max_depth__icontains=searched) | \
                 Spots.objects.filter(spot_category__name__icontains=searched)

    fish_data = Fish.objects.filter(name__icontains=searched) | \
                Fish.objects.filter(average_weight__icontains=searched) | \
                Fish.objects.filter(fish_category__name__icontains=searched)

    bait_data = Baits.objects.filter(name__icontains=searched) | \
                Baits.objects.filter(price__icontains=searched)

    if request.method == 'POST' and searched != '':
        context['data'] = [*spots_data, *fish_data, *bait_data]

    return render(request, 'spots/search.html', context)
