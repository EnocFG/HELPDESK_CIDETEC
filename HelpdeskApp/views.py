from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Ticket


# Create your views here.

def home(request):

    all_tickets = Ticket.newmanager.all()

    return render(request, 'index.html', {'tickets': all_tickets})


def ticket_single(request,ticket):

    ticket = get_object_or_404(Ticket, slug=ticket, status='published')

    return render(request, 'single.html', {'ticket': ticket})
