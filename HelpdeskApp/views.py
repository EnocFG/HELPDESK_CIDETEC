from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .forms import NewCommentForm

from .models import Ticket, Comentario

import requests
# Create your views here.
import json

from .serializers import TicketSerializer
from rest_framework import generics

class TicketAPI(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

def home(request):

    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)

    all_tickets = Ticket.newmanager.all()

    return render(request, 'index.html', {'tickets': all_tickets,
                                          'data': location_data
                                          })


def ticket_single(request, ticket):

    ticket = get_object_or_404(Ticket, slug=ticket, status='published')

    comments = NewCommentForm

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.ticket = ticket
            user_comment.save()
            return HttpResponseRedirect('/' + ticket.slug)
    else:
        comment_form = NewCommentForm()

    return render(request, 'single.html', {'ticket': ticket,
                                           'comments': user_comment,
                                           'comments': comments,
                                           'comment_form': comment_form
                                           })

