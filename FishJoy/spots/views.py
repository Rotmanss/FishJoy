from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from rest_framework import generics, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .forms import *
from .models import *
from .permissions import IsOwnerOrAdmin
from .serializer import *
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
        return Spots.objects.order_by('-rating', 'pk').select_related('spot_category')


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


def like_action(request, spot_slug):
    mixin = DataMixin()
    current_url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        spot = get_object_or_404(Spots, slug=spot_slug)
        spot.likes += 1
        spot.save()
        spot.rating = spot.calculate_rating()
        spot.save()
    return redirect(current_url)


def dislike_action(request, spot_slug):
    mixin = DataMixin()
    current_url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        spot = Spots.objects.get(slug=spot_slug)
        spot.dislikes += 1
        spot.save()
        spot.rating = spot.calculate_rating()
        spot.save()
    return redirect(current_url)


# Django REST Framework

class SpotsViewSet(viewsets.ModelViewSet):
    queryset = Spots.objects.all()
    serializer_class = SpotsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrAdmin)
        else:
            permission_classes = (IsAuthenticatedOrReadOnly,)
        return (permission() for permission in permission_classes)

    @action(methods=['get'], detail=False)
    def categories(self, request):
        cats = SpotCategory.objects.all()
        return Response({'cats': [c.name for c in cats]})

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cat = SpotCategory.objects.get(pk=pk)
        return Response({'cat': cat.name})


class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrAdmin)
        else:
            permission_classes = (IsAuthenticatedOrReadOnly,)
        return (permission() for permission in permission_classes)

    @action(methods=['get'], detail=False)
    def categories(self, request):
        cats = FishCategory.objects.all()
        return Response({'cats': [c.name for c in cats]})

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cat = FishCategory.objects.get(pk=pk)
        return Response({'cat': cat.name})


class BaitsViewSet(viewsets.ModelViewSet):
    queryset = Baits.objects.all()
    serializer_class = BaitsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrAdmin)
        else:
            permission_classes = (IsAuthenticatedOrReadOnly,)
        return (permission() for permission in permission_classes)
