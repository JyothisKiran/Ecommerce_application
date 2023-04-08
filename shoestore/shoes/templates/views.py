import json
from django.db.models import Q
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Book, Reggister, Loggin, Order


# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'list.html'


class BookDetailView(DetailView):
    model = Book
    fields = '__all__'
    template_name = 'detail.html'


class BookCheckoutView(DetailView):
    model = Book
    template_name = 'checkout.html'


class BookLoginView(LoginView):
    model = Loggin
    success_url = reverse_lazy('list')
    template_name = 'login.html'


class BookRegisterView(CreateView):
    model = Reggister
    form_class = UserCreationForm
    success_url = reverse_lazy('loggin')
    template_name = 'register.html'


def PaymentComplete(request):
    body=json.loads(request.body)
    print('BODY:',body)
    product=Book.objects.get(id=body['prosuctId'])
    Order.objects.create(product=product)
    return JsonResponse('Payment completed',safe=False)


class SearchResultsView(ListView):
    model = Book
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title=query) | Q(title=query))
