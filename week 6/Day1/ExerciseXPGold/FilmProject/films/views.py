from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import Film, Country, Category, Director, Review
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import FilmForm, DirectorForm, ReviewForm


# Create your views here.


class HomePageView(ListView):
    template_name = "homepage.html"
    context_object_name = "films"

    def get_queryset(self):
        return Film.objects.all()


class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = "film/add_film.html"
    success_url = reverse_lazy("homepage")


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = "director/add_director.html"
    success_url = reverse_lazy("homepage")


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "review/add_review.html"
    success_url = reverse_lazy("homepage")


class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = "film/film_edit.html"
    success_url = reverse_lazy("homepage")


class DirectorUpdateView(UpdateView):
    model = Director
    form_class = DirectorForm
    template_name = "director/director_edit.html"
    success_url = reverse_lazy("homepage")
