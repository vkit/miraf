from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, View, DetailView
from .models import Book, BookComment
from .forms import BookForm
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
import datetime
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin


class BookList(ListView):
    template_name = 'book_list.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        # context['form'] = TicketForm()
        # context['pending_count'] = Ticket.objects.filter(
        #     status='PENDING').count()
        # context['solved_count'] = Ticket.objects.filter(
        #     status='SOLVED').count()
        # context['closed_count'] = Ticket.objects.filter(
        #     status='CLOSED').count()
        # context['total_ticket'] = Ticket.objects.count()
        context['books'] = Book.objects.all().order_by('-created_at')
        # context['user'] = self.request.user
        # context['date'] = datetime.datetime.now()
        print "I am heretoo"
        return context
